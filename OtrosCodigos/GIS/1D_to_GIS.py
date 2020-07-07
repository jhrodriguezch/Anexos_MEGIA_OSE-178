#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:35:51 2020

@author: girehe2o
Obj: Generar los rasters a partir de los datos 1D
"""
# Lectura de los puntos de interes

import pandas as pd
import os
from EXT_Z_est import EXT_Z_est


os.chdir('../DATA/')
db_pnt_cienaga = pd.read_csv('Pnt_cienagas.csv')

os.chdir('../RESULT/')
db_result_m1d_h = pd.read_csv('H_msnm_3116.csv')
db_sta = pd.DataFrame()

for ii in db_pnt_cienaga['Abs']:
    h_pnt = EXT_Z_est(ii, list(db_result_m1d_h['Abs']), db_result_m1d_h[db_result_m1d_h.columns[:-1]].copy())
    h_pnt = h_pnt.values[0][1:]
    db_sta [ii] = h_pnt

db_sta.to_csv('data_serie_cienaga.csv', index = False)

'C:/PROGRA~1/QGIS3~1.10/apps/qgis/./python\\qgis\\core\\__init__.py'
