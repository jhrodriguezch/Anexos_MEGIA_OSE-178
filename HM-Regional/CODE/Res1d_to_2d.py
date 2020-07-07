#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:15:09 2020

@ author: girehe2o
@ Obj: Extraer los resultados del modelo 1d para usarlos como condicion de frontera 
    del modelo 2d
    
@ Notas:
    - Solo se estraen caudales aguas arriba y niveles aguas abajo, el numero de Strickler se 
    extrae para el sector completo para la modelación 2d
    - Además se extraen los datod de niveles aguas abajo, caudales aguas arriba y alturas a 
    traves del cause de análisis con la finalidad de generar una comparacón posterior (aun en
    desarrollo)
    - Al momento de la ejecución se ejecutan todo el script, lo que quiere decir que, no se
    requiere cambio de path
        
"""
import os
import pandas as pd
from EXT_Z_est import EXT_Z_est

def Res1d_to_2d ():
    
    os.chdir('../DATA/')
    db_points_boundary = pd.read_csv('Pnt_interconecion_1d_2d.csv')
    db_strickler_data = pd.read_csv('strikler.csv')
    
    os.chdir('../RESULTS/')
    db_result_m1d_h = pd.read_csv('H_msnm_3116.csv')
    db_result_m1d_q = pd.read_csv('Q_m3ps_3116.csv')
    
    # Busqueda del número de Strickler
    Abs_ini = db_points_boundary['ABS(m)'].iloc[0]
    Abs_fin = db_points_boundary['ABS(m)'].iloc[1]
    
    # Debe ser cambiado para depender de los puntos
    Str_sec = pd.DataFrame()
    Str_sec['Strickler'] = [db_strickler_data['strikler'].loc[3]]
    
    # Extracción de datos
    q_ini_2d = EXT_Z_est(Abs_ini, list(db_result_m1d_q['Abs']), db_result_m1d_q[db_result_m1d_q.columns[:-3]].copy())
    q_fin_2d = EXT_Z_est(Abs_fin, list(db_result_m1d_q['Abs']), db_result_m1d_q[db_result_m1d_q.columns[:-3]].copy())
    
    h_ini_2d = EXT_Z_est(Abs_ini, list(db_result_m1d_h['Abs']), db_result_m1d_h[db_result_m1d_h.columns[:-3]].copy())
    h_fin_2d = EXT_Z_est(Abs_fin, list(db_result_m1d_h['Abs']), db_result_m1d_h[db_result_m1d_h.columns[:-3]].copy())
    
    # Imprimir los datos
    q_ini_2d.to_csv('Q_2d_ini.csv', index = False)
    h_fin_2d.to_csv('H_2d_fin.csv', index = False)
    Str_sec.to_csv ('S_2h_i2f.csv', index = False)
    return(0)

#Res1d_to_2d()

# import matplotlib.pyplot as plt
#
# a = EXT_Z_est(280000, list(db_result_m1d_h['Abs']), db_result_m1d_h[db_result_m1d_h.columns[:-3]].copy())
# b = EXT_Z_est(320000, list(db_result_m1d_h['Abs']), db_result_m1d_h[db_result_m1d_h.columns[:-3]].copy())
#
# plt.plot(list(a.T[0][1:]), '.b', label = 'Aguas arriba')
# plt.plot(list(b.T[0][1:]), '.c', label = 'Aguas abajo')
# plt.legend()
# plt.grid()
# plt.ylabel('Nivel del rio - msnm')
# plt.xlabel('Dia de modelacion')
# plt.show()
