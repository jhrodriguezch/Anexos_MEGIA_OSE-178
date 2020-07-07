#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:15:05 2019

@author: girehe2o
Requiere: 
    - Numpy
    - Pandas
Obj: convertir el fichero .lis de mascaret a dataframes organizados dependiendo
de la variable que maneja el fichero resultado
"""

import pandas as pd
import numpy as np

def nest2df(file_name) :
    
    arc_brt = []
    arc_dfm = pd.DataFrame()
    
    # Cargar archivo al entorno
    archivo = file_name + '_NEST.lis'
    arch = open(archivo)
    for i in arch.readlines():
        arc_brt.append(str(i))
    arch.close()
    
    # indices de cada paso de tiempo, -8 paso de tiempo, -5 información general 
    arc_dfm = "  I     X        ZREF     Z        QF       QB       KMIN     KMAJ     FR       Q    \n"
    indices = [i for i, x in enumerate(arc_brt) if x == arc_dfm]
    
    # Número de pasos de tiempo
    n_paso_tiempo_temp = str(arc_brt[indices[14]-5]).strip()
    
    # Numero de pasos espaciales
    str_pt = ''
    prb = 'prb'
    i = -1
    while prb != ' ':
        str_pt += n_paso_tiempo_temp[i]
        i -= 1
        prb = n_paso_tiempo_temp[i]
        
    n_paso_tiempo = int(str_pt[::-1])
    
    # Cración de los df con los resultados
    
    df_Z = pd.DataFrame()
    df_Q_MIN = pd.DataFrame()
    df_Q_MAJ = pd.DataFrame()
    df_K_MIN = pd.DataFrame()
    df_K_MAJ = pd.DataFrame()
    df_FR = pd.DataFrame()
    df_Q = pd.DataFrame()
    
    # lista con los resultados para cada paso de tiempo
    for i in np.arange(0, len(indices)):
        tabla_data = arc_brt[indices[i] + 1 : indices[i] + n_paso_tiempo + 1]
        t_dia = arc_brt[indices[i] - 8][7: 12]
        t_hor = arc_brt[indices[i] - 8][20: 24]
        t_min = arc_brt[indices[i] - 8][33: 37]
        t_sec = arc_brt[indices[i] - 8][47: 51]
        Nomb_col = t_dia + t_hor + t_min + t_sec
        I = []
        X = []
        Z_REF = []
        T_Z = []
        T_Q_MIN = []
        T_Q_MAJ = []
        T_K_MIN = []
        T_K_MAJ = []
        T_FR = []
        T_Q = []
        for i in tabla_data:
            I.append(int(i[0 : 5]))
            X.append(float(i[5:16]))
            Z_REF.append(float(i[16:26]))
            T_Z.append(float(i[26:34]))
            T_Q_MIN.append(float(i[34:43]))
            T_Q_MAJ.append(float(i[43:52]))
            T_K_MIN.append(float(i[52:59]))
            T_K_MAJ.append(float(i[59:66]))
            T_FR.append(float(i[66:75]))
            T_Q.append(float(i[75:84]))
        
        df_Z[Nomb_col] = T_Z
        df_Q_MIN[Nomb_col] = T_Q_MIN
        df_Q_MAJ[Nomb_col] = T_Q_MAJ
        df_K_MIN[Nomb_col] = T_K_MIN
        df_K_MAJ[Nomb_col] = T_K_MAJ
        df_FR[Nomb_col] = T_FR
        df_Q[Nomb_col] = T_Q
    
    return(X, Z_REF, df_Z, df_Q_MIN, df_Q_MAJ, df_K_MIN, df_K_MAJ, df_FR, df_Q)

#prb = os.chdir('/home/girehe2o/Escritorio/MEGIA/M1D/M1D_EST_NES/NEST')
#X, Z_REF, df_Z, df_Q_MIN, df_Q_MAJ, df_K_MIN, df_K_MAJ, df_FR, df_Q = nest2df('MEGIA')