# -*- coding: utf-8 -*-
"""
by: IC Jhonatan Rodriguez Chaves

Obj: Make swamp rasters with Mascaret model 
"""
import pandas as pd
import numpy as np
import os

from osgeo import gdal
from osgeo.gdalconst import GA_Update

def Crear_raster(fn, fn_result, h_med, h_min):

    DEM = gdal.Open(fn)
    db_DEM = DEM.GetRasterBand(1).ReadAsArray()
    db_DEM_1 = np.array(db_DEM)
    if h_med >= h_min:
        db_DEM_1 = (db_DEM_1 <= h_med) * db_DEM
    else:
        db_DEM_1 = (db_DEM_1 <= h_min) * db_DEM
        
    # Crear el nuevo tiff
    os.chdir('../RESULT/GIS/')
    
    ds_temp = gdal.Open(fn_result)
    driver_tiff = gdal.GetDriverByName('GTiff')
    ds_temp = driver_tiff.Create(fn_result, xsize = db_DEM.shape[1],
                            ysize = db_DEM.shape[0],
                            bands = 1,
                            eType = gdal.GDT_Float32)
    ds_temp.SetGeoTransform(DEM.GetGeoTransform())
    ds_temp.SetProjection(DEM.GetProjection())
    ds_temp.GetRasterBand(1).WriteArray(db_DEM_1)    
    DEM = None
    ds_temp = None
    
    nodata = 0
    ds = gdal.Open(fn_result, GA_Update)
    ds.GetRasterBand(1).SetNoDataValue(nodata)
    ds = None
    
    os.chdir('../../DATA')
    
    db_DEM_ana = db_DEM_1
    db_DEM_ana[db_DEM_ana != 0] = 1
    debug_line = 'Cienaga ' + fn[:-12] + ': ' +  str(db_DEM_ana.sum() * 12.5 / 1000 * 12.5 / 1000) + ' km2'
    return(db_DEM_1, debug_line)

# Programa principal
db = pd.read_csv('C:/Users/57314/Desktop/MEGIA_1D_2D/RESULT/data_serie_cienaga.csv')
os.chdir('C:\\Users\\57314\\Desktop\\MEGIA_1D_2D\\DATA')
os.chdir('../DATA/')

db_2 = pd.read_csv('V1_Tbl_Cienagas_Centroides.csv', sep = ';')
coor_y_x = db[db.columns][-2:].copy()

# 
summary_file = []
summary_file.append(70 * '-')

for ii in np.linspace(0, len(db[db.columns[0]]) - 1, len(db[db.columns[0]])):

    # Data for some day
    data_work = pd.DataFrame()
    data_diary = db.iloc[int(ii)].copy()
    data_work ['absc'] = data_diary.index
    data_work ['high'] = data_diary.values

    # Data from GIS
    abs_gis = np.unique(db_2['Abs_conec'])
    high = []
    data_diary = pd.DataFrame()
    for jj in abs_gis:
        high.append(data_work[data_work['absc'] == str(jj)]['high'].values[0])

    data_diary['absc'] = abs_gis
    data_diary['high'] = high

    #print('Dia de modelacion: ' + str(ii))
    summary_file.append('Dia de modelacion: ' + str(ii))

    high_2 = []
    for jj in np.linspace(0, len(db_2) - 1, len(db_2)):
        high_2.append(data_diary[data_diary['absc'] == db_2['Abs_conec'].iloc[int(jj)]]['high'].values[0])
    result = pd.DataFrame()
    result ['Abs'] = db_2['Abs_conec']
    result ['x'] = db_2['X']
    result ['y'] = db_2['y']
    result ['h'] = high_2

    # TIF ANALYSIS
    # NOTAS:
    #1. Alturas minimas en cada Complejo de cienagas
    # - 34100 - 101 m 
    # - 42400 - 95 m 
    # - 161500 - 55 m
    # - 168400 - 45 m
    # - 255100 - 37
    # - 278500 - 37
    # - 305100 - 33
    # - 307400 - 33
    # - 341500 - 25

    # -----------------------------    
    fn = '34100_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 34100]['h'].values[0]
    h_min = 101
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------    
    fn = '42400_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 34100]['h'].values[0]
    h_min = 101
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------
    fn = '161500_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 161500]['h'].values[0]
    h_min = 55
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------       
    fn = '168400_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 168400]['h'].values[0]
    h_min = 50
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------  
    fn = '255100_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 255100]['h'].values[0]
    h_min = 37
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------
    fn = '278500_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 278500]['h'].values[0]
    h_min = 37
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------    
    fn = '305100_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 305100]['h'].values[0]
    h_min = 33
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------  
    fn = '307400_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 307400]['h'].values[0]
    h_min = 33
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------
    fn = '341500_Cienaga.tif'
    fn_result = fn[:-4] + '_res_' + str(int(ii)) + '.tif'
    h_med = result[result['Abs'] == 341500]['h'].values[0]
    h_min = 25
    db_res, line = Crear_raster(fn, fn_result, h_med, h_min)
    summary_file.append(line)
    # -----------------------------    
    summary_file.append(70 * '-')

os.chdir('../RESULT/')
summary_file_pd = pd.DataFrame()
summary_file_pd['INFORME GENERAL'] = summary_file
summary_file_pd.to_csv('analisis_cienagas_resumen.txt', index = False)
print(result)
