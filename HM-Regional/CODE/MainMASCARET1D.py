#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:57:47 2019

@author: jhrodriguezch
Obj: Proyecto MEGIA - evaluación general del modelo 1D
Requiere:
    Codigos
        - sol2Serie.py
        - SolCorr.py
        - soldf2lig
    
Notas:
    28/02/2020 -Cambio del scrip nest2df por FilterResult, ya que este ultimo
                funciona linea a linea y permite la lectura y acumulacion de 
                los datos modelados a nivel diario
    28/02/2020 -No se requiere el uso de la libreria z_acum, remplazada 
                exitosamente
    
"""
# Librerias generales

import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def MainMASCARET1D():
    # Librerias específicas desarrolladas
    import os
    os.chdir('/home/girehe2o/Escritorio/MEGIA_MODEL/CODE')
    
    from crearXCAS import crearXCAS
    from EXT_Z_est import EXT_Z_est
    from M1D2HG_3116 import M1D2HG
    from nest2df import nest2df
    from Sol2Serie import * #main_function_sol2serie as Sol2Serie
    from SolCorr import * #main_function_seriecorr as SolCorr
    from soldf2lig import soldf2lig
#    from z_acum import z_acum
    from FilterResults import FilterResults

    # -----------------------------------------------------------------------------
    # ------------------- VARIABLES -----------------------------------------------
    # -----------------------------------------------------------------------------
    
    # Variables. Ubicación de archivos
    print('---------------- PROGRAMA INICIADO ----------------')
    t0 = time.time()
    file_name = "MEGIA"
    PATH_EST = "/home/girehe2o/Escritorio/MEGIA_MODEL/00_EST"
    PATH_NEST = "/home/girehe2o/Escritorio/MEGIA_MODEL/00_NEST"
    
    # Variables del modeloZ_4326 ['Abs'] = X
    # Vector con manin inicial(9%) CHECK
    # Número de Manning en el canal a modelar - Ver carpeta DATOS
    
    os.chdir('../DATA')
    strk_brt = pd.read_csv('Strk_data.csv', index_col = False)
    
    abz_cort = list( strk_brt['Abz_fin_m'])
    abz_cort.insert(0, strk_brt['Abz_ini_m'][0])
    coef_Strk = list(strk_brt['Coef_Strk'].values )
    
    #abz_cort = [0, 90838, 125686, 140069, 176823, 198248, 230469, 237946, 276599, 283232, 362000] #Valor de abscisado
    #coef_Strk = [27.03, 27.78, 32.26, 33.33, 33.33, 33.33, 33.33, 33.33, 25.81, 25.81]
    
    # Caudales de entrada al canal principal --- 
    # Caudales fijos
    # Obtenidos directamente del modelo hidrologico, por lo cual son archivos creados
    # previamente. Los cambios en los caudales estan determinados. 
    
    # Caudales dinámicos
    # Obtenidos del modelo hidrológico, cambian en cada simulación de este. requie
    # actualización continua.
    
    # -----------------------------------------------------------------------------
    # ----------------- ANÄLISIS ESTACIONARIO -------------------------------------
    # -----------------------------------------------------------------------------
    
    prb = os.chdir(PATH_EST)
    
    # Eliminación de archivos previos
    try: 
        rm_pre_file = r"rm *.txt *.rub *.lis"
        subprocess.check_call(rm_pre_file, shell = True)
    except:
            print('Primer corrida estacionaria')
    
    # Generar el .xcas con números de manning determinados
    prb = crearXCAS( 'MEGIA_EST.xcas', 1, abz_cort, coef_Strk)
    
    # Correr el modelo
    masc_sis = r"mascaret.py MEGIA_EST.xcas"
    subprocess.check_call(masc_sis, shell = True)
    
    t = time.time() - t0
    print('Fin estacionario. Tiempo: ' +str(t))
    
    # Caudales de entrada
    
    # Convierte archivo .rub en dataframe
    soldf = main_function_sol2serie(str(file_name+'_EST.rub'))
    
    # Separación por momentos
    soldf, N_paso = main_function_seriecorr(soldf)
    
    # -----------------------------------------------------------------------------
    # --------------- ANÄLISIS NO ESTACIONARIO ------------------------------------
    # -----------------------------------------------------------------------------
    
    # Crear el archivo con de valores iniciales .lig
    prb = os.chdir(PATH_NEST)
    
    check_arc_lig = soldf2lig(soldf, N_paso, file_name)
    # ¡Warning! se genera el archivo temp.lig ---> Borrar, contiene la solución pero pesa mucho
    
    # Generar el .xcas para correr el modelo en condiciones no estacionarias (non-stedy)
    arch_NEST = 'MEGIA_NEST'
    
    crearXCAS( arch_NEST + '.xcas', 2, abz_cort, coef_Strk)
    try: 
        rm_pre_file = r"rm *.txt *.rub *.lis"
        subprocess.check_call(rm_pre_file, shell = True)
    except:
            print('Primer corrida no estacionaria')
    
    # Correr M1D NEST
    masc_sis = r'mascaret.py ' + arch_NEST + '.xcas'
    subprocess.check_call(masc_sis, shell=True)
    
    t = time.time() - t0
    print('Fin no estacionario. Tiempo: ' +str(t))
    
    # Obsoleta --- leer resultados de la condicion inestable y generar vector
    # X, Zref, Z, Qmin, Qmaj, Kmin, Kmsj, Fr, Q = nest2df(file_name) 
    
    # Cambio del scrip nest2df por FilterResult
    X, b, b, b, b, b, b, b, b = FilterResults(file_name, 'x')
    b, Zref, b, b, b, b, b, b, b = FilterResults(file_name, 'zref')
    b, b, Z, b, b, b, b, b, Q = FilterResults(file_name, 'q')    
    
    t = time.time() - t0
    print('Fin analisis de resultados. Tiempo: ' +str(t))
    
    # -----------------------------------------------------------------------------
    # ----------------- ANALISIS DE RESULTADOS ------------------------------------
    # -----------------------------------------------------------------------------
    
    # Georeferenciación de los puntos en el thalweg
    os.chdir(PATH_NEST)
    os.chdir('../DATA')
    import os
    Abz_c = []
    Lat_c = []
    Lon_c = []
    
    Abz_xy = []
    X_c = []
    Y_c = []
    
    for i in X:
        dummy_1, dummy_2, dummy_3, dummy_4, dummy_5, dummy_6 = M1D2HG (i)
        Abz_c.append(dummy_1)
        Lat_c.append(dummy_2)
        Lon_c.append(dummy_3)
        Abz_xy.append(dummy_4)
        X_c.append(dummy_5)
        Y_c.append(dummy_6)
    
    # Obsoleto -- Organización datos Z para acumulación
#    Z_mod = Z.copy()
#    Z = z_acum(Z)
#    
#    Q_mod = Q
#    Q = z_acum(Q)
    
    t = time.time() - t0
    print('Fin organizacion de datos. Tiempo: ' +str(t))
    
    # Impresión de resultados
    os.chdir('../RESULTS/')
    
    name_arch_3116 = 'H_msnm_3116.csv'
    name_arch_4326 = 'H_msnm_4326.csv'
    
    name_arch_q_3116 = 'Q_m3ps_3116.csv'
    name_arch_q_4326 = 'Q_m3ps_4326.csv'
    
    Z_4326 = Z.copy()
    Z_3116 = Z.copy()
    Z_4326 ['Lat'] = Lat_c
    Z_4326 ['Lon'] = Lon_c
    Z_4326 ['Abs'] = X
    Z_3116 ['X'] = X_c
    Z_3116 ['Y'] = Y_c
    Z_3116 ['Abs'] = X
    
    Q_4326 = Q.copy()
    Q_3116 = Q.copy()
    Q_4326 ['Lat'] = Lat_c
    Q_4326 ['Lon'] = Lon_c
    Q_4326 ['Abs'] = X
    Q_3116 ['X'] = X_c
    Q_3116 ['Y'] = Y_c
    Q_3116 ['Abs'] = X
    
    Z_4326.to_csv(name_arch_4326, header = True, index = None)
    Z_3116.to_csv(name_arch_3116, header = True, index = None)
    
    Q_4326.to_csv(name_arch_q_4326, header = True, index = None)
    Q_3116.to_csv(name_arch_q_3116, header = True, index = None)
    
    t = time.time() - t0
    print('Fin impresión de resultados ' + str(t))
        
    return (0)
 
#MainMASCARET1D()
