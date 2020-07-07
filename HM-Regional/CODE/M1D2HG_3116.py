#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:33:07 2019

@author: IC Jhonatan Rodriguez Chaves
Requerimiento:
    Libtrerias:

        - pandas
        - numpy
"""
import pandas as pd
import numpy as np

def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 

def M1D2HG (abz):
    
    # Path donde esta ./datos con la base de datos Talve_db.csv
    #path = '/home/girehe2o/Escritorio/MEGIA/M1D/M1D2HG'
    #os.chdir(path)
    
    # Cargar base de datos
#    path = os.getcwd()
#    os.chdir(path + '/data_M1D2HG')
#    print(os.listdir(os.getcwd()) )
#    os.chdir('./data_M1D2HG/')
    db = pd.read_csv('Talve_db.csv')
    
    vec = db ['D_geo_acum_km'].copy() * 1000
    
    # Valor de abcizado
    num_m = abz # 367677.947
    #num_m = 367000.000
    
    # Busqueda en la base de datos
    f = []
    f.append(max(vec[vec <= num_m]))
    f.append(min(vec[vec >= num_m]))
    
    # Estracción de los valores cercanos (Latitud - longitud)
    p1_abz = f[0]
    lat0_d, lon0_d = db[vec == p1_abz]['Lat_4326_rad'], db[vec == p1_abz]['Lon_4326_rad']
    lat0_r, lon0_r = lat0_d.values[0] * (np.pi / 180), lon0_d.values[0] * (np.pi / 180)
    
    p2_abz = f[1]
    lat1_d, lon1_d = db[vec == p2_abz]['Lat_4326_rad'], db[vec == p2_abz]['Lon_4326_rad']
    lat1_r, lon1_r = lat1_d.values[0] * (np.pi / 180), lon1_d.values[0] * (np.pi / 180)
    
    # Extracción de los valores cercanos (X e Y)
    Y0 = db[vec == p1_abz]['Y'].copy()
    Y0 = Y0.values[0]
    X0 = db[vec == p1_abz]['X'].copy()
    X0 = X0.values[0]
    
    Y1 = db[vec == p2_abz]['Y'].copy()
    Y1 = Y1.values[0]
    X1 = db[vec == p2_abz]['X'].copy()
    X1 = X1.values[0]
    
    # Puntos intermedios entre los puntos encontrados (Latitud - Longitud)
    n_pasos = 10000
    
    if lat0_r == lat1_r:
        dummy = np.ones(n_pasos)
        dummy = lat0_r * dummy
        lat = np.array(dummy)
    else:
        dummy = []
        for i in np.arange(0, n_pasos): dummy.append(i)
        dummy = np.array(dummy)
        lat = lat0_r + (lat1_r - lat0_r) / n_pasos * dummy
    
    if lon1_r == lon0_r:
        dummy = np.ones(n_pasos)
        dummy = lon1_r * dummy
        lon = np.array(dummy)
    else:
        dummy = []
        for i in np.arange(0, n_pasos): dummy.append(i)
        dummy = np.array(dummy)
        lon = lon0_r + (lon1_r - lon0_r) / n_pasos * dummy
    
    # Puntos intermedios entre los puntos encontrados (Y - X)
    if Y0 == Y1:
        dummy = np.ones(n_pasos)
        dummy = Y0 * dummy
        Y = np.array(dummy)
    else:
        dummy = []
        for i in np.arange(0, n_pasos): dummy.append(i)
        dummy = np.array(dummy)
        Y = Y0 + (Y1 - Y0) / n_pasos * dummy
    
    if X1 == X0:
        dummy = np.ones(n_pasos)
        dummy = X1 * dummy
        X = np.array(dummy)
    else:
        dummy = []
        for i in np.arange(0, n_pasos): dummy.append(i)
        dummy = np.array(dummy)
        X = X0 + (X1 - X0) / n_pasos * dummy
    
    # Calculo de distancias internas de los puntos antes generados
    dis_xy = p1_abz + np.sqrt((X - X0) ** 2 + (Y - Y0) ** 2)
#    dis = p1_abz + (6378000 * np.arccos(np.sin(lat0_r) * np.sin(lat) + np.cos(lat0_r) * np.cos(lat) * np.cos(lon0_r - lon)))
    
    diff_lon = lon - lon0_r
    diff_lat = lat - lat0_r 
    a = np.power(np.sin((1/2.)*diff_lat) ,2) + np.multiply(np.multiply(np.cos(lat) ,np.cos(lat0_r)), np.power(np.sin((1/2.) * diff_lon) , 2))
    c = 2 * np.arctan2(np.sqrt(a) ,np.sqrt(1 -a))
    dis = p1_abz + 6373000 * c
    
    dis_xy[-1] = f[1]
    dis[-1] = f[1]
    
    """ 17/02/2020el vector calculado dis (tanto dis como dis_xy) no posee los limites
    de las longitudes que deberian dar segun los limites establecidos por el vector f,
    esto se pudede deber a errores computacionales debido al número de cifras significa_
    tivas a tratar.     
    """
    
    # Selección de los puntos más cercanos, Latitud - Longitud
    f_1 = []
    f_1.append(max(dis[dis <= num_m]))
    f_1.append(min(dis[dis >= num_m]))
    
    # Selección de los puntos más cercanos, Latitud - Longitud
    f_1_xy = []
    f_1_xy.append(max(dis_xy[dis <= num_m]))
    f_1_xy.append(min(dis_xy[dis >= num_m]))
    
    lat = lat * (180 / np.pi)
    lon = lon * (180 / np.pi)
    
    # Extraer latitud y longitud
    lat_new = lat[ dis == f_1[0]]
    lon_new = lon[ dis == f_1[0]]
    
    # Extraer X e Y
    Y_new = Y[dis_xy == f_1_xy[0]]
    X_new = X[dis_xy == f_1_xy[0]]

    return(f_1[0], lat_new[0], lon_new[0], f_1_xy[0], Y_new[0], X_new[0])