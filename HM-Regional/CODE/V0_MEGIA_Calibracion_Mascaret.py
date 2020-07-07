#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:46:42 2020

@author: IC Jhonatan R
Obj: Calibrar de manera simple el modelo mascaret - MEGIA

06/02/2020 - V.0. - Calibración manual cuya finalidad es brindar limites de calibración
"""
# Librerias

import os
import pandas as pd
import numpy as np

from MainMASCARET1D import MainMASCARET1D
from EXT_Z_est import EXT_Z_est

def NS(s, o):
    """
        Nash Sutcliffe efficiency coefficient
        input:
        s: simulated
        o: observed
        output:
        ns: Nash Sutcliffe efficient coefficient
        """
    return (1 - np.sum((s-o)**2)/np.sum((o-np.mean(o))**2))

def rmse(s, o):
    return(np.sqrt(np.mean((s - o) ** 2)))

def difr(s, o):
    top = np.abs(s - o)
    bot = np.sum(1 - np.isnan(top))
    return(np.sum(top) / bot)

# ------------------ Variables ------------------------
p_work = '/home/girehe2o/Escritorio/MEGIA_MODEL'
p_mode = '/home/girehe2o/Escritorio/MEGIA_MODEL/CODE'
ano_mod = 2013
n_mod = 20.
os.chdir(p_work)

# --------------- Lectura de datos observados ----------------------

lis_est = pd.read_csv('./DATA/V0_MEGIA_Estaciones_M1D.csv')

# Estacion BADI - Badillo
est_badi = pd.read_csv('./DATA/' + str(lis_est['FILE'][6]))
est_badi = est_badi[est_badi['ANO'] == ano_mod].copy()
est_badi = est_badi.reset_index(drop = True)
abz_badi = lis_est['ABSCISA'][6]
comp_badi = pd.DataFrame()

# Estacion BARR - Barrancabermeja
est_barr = pd.read_csv('./DATA/' + str(lis_est['FILE'][2]))
est_barr = est_barr[est_barr['ANO'] == ano_mod].copy()
est_barr = est_barr.reset_index(drop = True)
abz_barr = lis_est['ABSCISA'][2]
comp_barr = pd.DataFrame()

# Estacion ELCO - El Contento
est_elco = pd.read_csv('./DATA/' + str(lis_est['FILE'][7]))
est_elco = est_elco[est_elco['ANO'] == ano_mod].copy()
est_elco = est_elco.reset_index(drop = True)
abz_elco = lis_est['ABSCISA'][7]
comp_elco = pd.DataFrame()

# Estacion LAGL - la gloria
est_lagl = pd.read_csv('./DATA/' + str(lis_est['FILE'][8]))
est_lagl = est_lagl[est_lagl['ANO'] == ano_mod].copy()
est_lagl = est_lagl.reset_index(drop = True)
abz_lagl = lis_est['ABSCISA'][8]
comp_lagl = pd.DataFrame()

# Estacion PENO - Penonsito
est_peno = pd.read_csv('./DATA/' + str(lis_est['FILE'][10]))
est_peno = est_peno[est_peno['ANO'] == ano_mod].copy()
est_peno = est_peno.reset_index(drop = True)
abz_peno = lis_est['ABSCISA'][10]
comp_peno = pd.DataFrame()

# Estacion PUBE - Puerto berrio
est_pube = pd.read_csv('./DATA/' + str(lis_est['FILE'][0]))
est_pube = est_pube[est_pube['ANO'] == ano_mod].copy()
est_pube = est_pube.reset_index(drop = True)
abz_pube = lis_est['ABSCISA'][0]
comp_pube = pd.DataFrame()

# Estacion PUWI - Puerto Wilches
est_puwi = pd.read_csv('./DATA/' + str(lis_est['FILE'][3]))
est_puwi = est_puwi[est_puwi['ANO'] == ano_mod].copy()
est_puwi = est_puwi.reset_index(drop = True)
abz_puwi = lis_est['ABSCISA'][3]
comp_puwi = pd.DataFrame()

# Estacion SAPA - sanpablorio
est_sapa = pd.read_csv('./DATA/' + str(lis_est['FILE'][4]))
est_sapa = est_sapa[est_sapa['ANO'] == ano_mod].copy()
est_sapa = est_sapa.reset_index(drop = True)
abz_sapa = lis_est['ABSCISA'][4]
comp_sapa = pd.DataFrame()

# Estacion sinu - sitionuevo
est_sinu = pd.read_csv('./DATA/' + str(lis_est['FILE'][5]))
est_sinu = est_sinu[est_sinu['ANO'] == ano_mod].copy()
est_sinu = est_sinu.reset_index(drop = True)
abz_sinu = lis_est['ABSCISA'][5]
comp_sinu = pd.DataFrame()

# Estacion PEBA - Penasblancas
est_peba = pd.read_csv('./DATA/' + str(lis_est['FILE'][1]))
est_peba = est_peba[est_peba['ANO'] == ano_mod].copy()
est_peba = est_peba.reset_index(drop = True)
abz_peba = lis_est['ABSCISA'][1]
comp_peba = pd.DataFrame()

# Estacion REGI - Regidor
est_regi = pd.read_csv('./DATA/' + str(lis_est['FILE'][9]))
est_regi = est_regi[est_regi['ANO'] == ano_mod].copy()
est_regi = est_regi.reset_index(drop = True)
abz_regi = lis_est['ABSCISA'][9]
comp_regi = pd.DataFrame()

# ---- Comienza la calibración por medio de for--------------

# Lectura de coeficientes de Manning
strikler = pd.read_csv('./DATA/strikler.csv')

try:
    # badillo N
    coefNS_badi   = []
    coefRMSE_badi = []
    coefDIFR_badi = []
    # barrancabermeja N
    coefNS_barr   = []
    coefRMSE_barr = []
    coefDIFR_barr = []
    # elcontento N
    coefNS_elco   = []
    coefRMSE_elco = []
    coefDIFR_elco = []
    # lagloria N
    coefNS_lagl   = []
    coefRMSE_lagl = []
    coefDIFR_lagl = []
    # penonsito N
    coefNS_peno   = []
    coefRMSE_peno = []
    coefDIFR_peno = []
    # puertoberrio N
    coefNS_pube   = []
    coefRMSE_pube = []
    coefDIFR_pube = []
    # puertowilches N
    coefNS_puwi   = []
    coefRMSE_puwi = []
    coefDIFR_puwi = []
    # sanpablorio N
    coefNS_sapa   = []
    coefRMSE_sapa = []
    coefDIFR_sapa = []
    # sitionuevo N
    coefNS_sinu   = []
    coefRMSE_sinu = []
    coefDIFR_sinu = []
    # penasblancas Q
    coefNS_peba   = []
    coefRMSE_peba = []
    coefDIFR_peba = []
    # regidor Q
    coefNS_regi   = []
    coefRMSE_regi = []
    coefDIFR_regi = []
    
    # MEJORES VALORESOSTRICH 115 CALIBRACIÓN - Menor NASH
    # Sec_01 =  20.00000
    # Sec_02 =  53.85749
    # Sec_03 =  49.15501
    # Sec_04 =  95.42493
    # Sec_05 =  97.47607
    # Sec_06 =  59.60615
    # Sec_07 =  59.60615
    # Sec_08 =  41.08592
    # Sec_09 = 101.23900
    # Sec_10 = 101.23900
            
    f_strik_cond = pd.DataFrame()
    f_strik_cond['Abz_ini_m'] = np.array(strikler['abz'][:-1].copy())
    f_strik_cond['Abz_fin_m'] = np.array(strikler['abz'][1:].copy())
    f_strik_cond['Coef_Strk'] = np.array(strikler['strikler'].copy()[1:])
    
    #Plotear archivo
    os.chdir(p_mode)
    os.chdir('../DATA')
    f_strik_cond.to_csv('Strk_data.csv', index=False)
    
    # CORRER EL MODELO
    os.chdir(p_mode)
    aa = MainMASCARET1D()
    print('Fin corre el modelo')
    
    # Lectura de datos modelados
    os.chdir(p_mode)
    os.chdir('../RESULTS')
    
    
    z_mod = pd.read_csv('H_msnm_3116.csv')
    q_mod = pd.read_csv('Q_m3ps_3116.csv')

    mod_z_badi = EXT_Z_est(abz_badi, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_barr = EXT_Z_est(abz_barr, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_elco = EXT_Z_est(abz_elco, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_lagl = EXT_Z_est(abz_lagl, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_peno = EXT_Z_est(abz_peno, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_pube = EXT_Z_est(abz_pube, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_puwi = EXT_Z_est(abz_puwi, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_sapa = EXT_Z_est(abz_sapa, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_z_sinu = EXT_Z_est(abz_sinu, list(z_mod['Abs']), z_mod[z_mod.columns[:-3]].copy() )
    mod_q_peba = EXT_Z_est(abz_peba, list(q_mod['Abs']), q_mod[q_mod.columns[:-3]].copy() )
    mod_q_regi = EXT_Z_est(abz_regi, list(q_mod['Abs']), q_mod[q_mod.columns[:-3]].copy() )      
    
    obs_z_badi = est_badi['VALOR'][0:len(mod_z_badi.columns) - 1]
    obs_z_barr = est_barr['VALOR'][0:len(mod_z_barr.columns) - 1]
    obs_z_elco = est_elco['VALOR'][0:len(mod_z_elco.columns) - 1]
    obs_z_lagl = est_lagl['VALOR'][0:len(mod_z_lagl.columns) - 1]
    obs_z_peno = est_peno['VALOR'][0:len(mod_z_peno.columns) - 1]
    obs_z_pube = est_pube['VALOR'][0:len(mod_z_pube.columns) - 1]
    obs_z_puwi = est_puwi['VALOR'][0:len(mod_z_puwi.columns) - 1]    
    obs_z_sapa = est_sapa['VALOR'][0:len(mod_z_sapa.columns) - 1]
    obs_z_sinu = est_sinu['VALOR'][0:len(mod_z_sinu.columns) - 1]
    obs_q_peba = est_peba['VALOR'][0:len(mod_q_peba.columns) - 1]
    obs_q_regi = est_regi['VALOR'][0:len(mod_q_regi.columns) - 1]
        
    #count_jj.append(jj)
    
    # Análisis Estacion badi - z
    obs_z_badi = list(obs_z_badi)
    mod_z_badi = list(mod_z_badi.loc[0][1:])
    comp_badi ['mod'] = mod_z_badi
    comp_badi ['obs'] = obs_z_badi
    coefNS_badi.append(NS(comp_badi['mod'], comp_badi['obs']))
    coefRMSE_badi.append(rmse(comp_badi['mod'], comp_badi['obs']))
    coefDIFR_badi.append(difr(comp_badi['mod'], comp_badi['obs']))
    
    # Análisis Estacion BARR - z
    obs_z_barr = list(obs_z_barr)
    mod_z_barr = list(mod_z_barr.loc[0][1:])
    comp_barr ['mod'] = mod_z_barr
    comp_barr ['obs'] = obs_z_barr
    coefNS_barr.append(NS(comp_barr['mod'], comp_barr['obs']))
    coefRMSE_barr.append(rmse(comp_barr['mod'], comp_barr['obs']))
    coefDIFR_barr.append(difr(comp_barr['mod'], comp_barr['obs']))
    
    # Análisis Estacion ELCO - z
    obs_z_elco = list(obs_z_elco)
    mod_z_elco = list(mod_z_elco.loc[0][1:])
    comp_elco ['mod'] = mod_z_elco
    comp_elco ['obs'] = obs_z_elco
    coefNS_elco.append(NS(comp_elco['mod'], comp_elco['obs']))
    coefRMSE_elco.append(rmse(comp_elco['mod'], comp_elco['obs']))
    coefDIFR_elco.append(difr(comp_elco['mod'], comp_elco['obs']))
    
    # Análisis Estacion LAGL - z
    obs_z_lagl = list(obs_z_lagl)
    mod_z_lagl = list(mod_z_lagl.loc[0][1:])
    comp_lagl ['mod'] = mod_z_lagl
    comp_lagl ['obs'] = obs_z_lagl
    coefNS_lagl.append(NS(comp_lagl['mod'], comp_lagl['obs']))
    coefRMSE_lagl.append(rmse(comp_lagl['mod'], comp_lagl['obs']))
    coefDIFR_lagl.append(difr(comp_lagl['mod'], comp_lagl['obs']))
    
    # Análisis Estacion PENO - z
    obs_z_peno = list(obs_z_peno)
    mod_z_peno = list(mod_z_peno.loc[0][1:])
    comp_peno ['mod'] = mod_z_peno
    comp_peno ['obs'] = obs_z_peno
    coefNS_peno.append(NS(comp_peno['mod'], comp_peno['obs']))
    coefRMSE_peno.append(rmse(comp_peno['mod'], comp_peno['obs']))
    coefDIFR_peno.append(difr(comp_peno['mod'], comp_peno['obs']))
    
    # Análisis Estacion PUBE - z
    obs_z_pube = list(obs_z_pube)
    mod_z_pube = list(mod_z_pube.loc[0][1:])
    comp_pube ['mod'] = mod_z_pube
    comp_pube ['obs'] = obs_z_pube
    coefNS_pube.append(NS(comp_pube['mod'], comp_pube['obs']))
    coefRMSE_pube.append(rmse(comp_pube['mod'], comp_pube['obs']))
    coefDIFR_pube.append(difr(comp_pube['mod'], comp_pube['obs']))
    
    # Análisis Estacion PUWI - z
    obs_z_puwi = list(obs_z_puwi)
    mod_z_puwi = list(mod_z_puwi.loc[0][1:])
    comp_puwi ['mod'] = mod_z_puwi
    comp_puwi ['obs'] = obs_z_puwi
    coefNS_puwi.append(NS(comp_puwi['mod'], comp_puwi['obs']))  
    coefRMSE_puwi.append(rmse(comp_puwi['mod'], comp_puwi['obs']))
    coefDIFR_puwi.append(difr(comp_puwi['mod'], comp_puwi['obs']))  
    
    # Análisis Estacion SAPA - z
    obs_z_sapa = list(obs_z_sapa)
    mod_z_sapa = list(mod_z_sapa.loc[0][1:])
    comp_sapa ['mod'] = mod_z_sapa
    comp_sapa ['obs'] = obs_z_sapa
    coefNS_sapa.append(NS(comp_sapa['mod'], comp_sapa['obs']))
    coefRMSE_sapa.append(rmse(comp_sapa['mod'], comp_sapa['obs']))
    coefDIFR_sapa.append(difr(comp_sapa['mod'], comp_sapa['obs']))
    
    # Análisis Estacion SINU - z
    obs_z_sinu = list(obs_z_sinu)
    mod_z_sinu = list(mod_z_sinu.loc[0][1:])
    comp_sinu ['mod'] = mod_z_sinu
    comp_sinu ['obs'] = obs_z_sinu
    coefNS_sinu.append(NS(comp_sinu['mod'], comp_sinu['obs'])) 
    coefRMSE_sinu.append(rmse(comp_sinu['mod'], comp_sinu['obs'])) 
    coefDIFR_sinu.append(difr(comp_sinu['mod'], comp_sinu['obs'])) 
    
    # Análisis Estacion PEBA - Q
    obs_q_peba = list(obs_q_peba)
    mod_q_peba = list(mod_q_peba.loc[0][1:])
    comp_peba ['mod'] = mod_q_peba
    comp_peba ['obs'] = obs_q_peba
    coefNS_peba.append(NS(comp_peba['mod'], comp_peba['obs']))
    coefRMSE_peba.append(rmse(comp_peba['mod'], comp_peba['obs']))
    coefDIFR_peba.append(difr(comp_peba['mod'], comp_peba['obs']))
    
    # Análisis Estacion REGI - Q
    obs_q_regi = list(obs_q_regi)
    mod_q_regi = list(mod_q_regi.loc[0][1:])
    comp_regi ['mod'] = mod_q_regi
    comp_regi ['obs'] = obs_q_regi
    coefNS_regi.append(NS(comp_regi['mod'], comp_regi['obs']))
    coefRMSE_regi.append(rmse(comp_regi['mod'], comp_regi['obs']))
    coefDIFR_regi.append(difr(comp_regi['mod'], comp_regi['obs']))
    
    print('El trabajo ha sido terminado')
except:
    # Badillo N
    coefNS_badi   = []
    coefRMSE_badi = []
    coefDIFR_badi = []
    # barrancabermeja N
    coefNS_barr   = []
    coefRMSE_barr = []
    coefDIFR_barr = []
    # elcontento N
    coefNS_elco   = []
    coefRMSE_elco = []
    coefDIFR_elco = []
    # lagloria N
    coefNS_lagl   = []
    coefRMSE_lagl = []
    coefDIFR_lagl = []
    # penonsito N
    coefNS_peno   = []
    coefRMSE_peno = []
    coefDIFR_peno = []
    # puertoberrio N
    coefNS_pube   = []
    coefRMSE_pube = []
    coefDIFR_pube = []
    # puertowilches N
    coefNS_puwi   = []
    coefRMSE_puwi = []
    coefDIFR_puwi = []
    # sanpablorio N
    coefNS_sapa   = []
    coefRMSE_sapa = []
    coefDIFR_sapa = []
    # sitionuevo N
    coefNS_sinu   = []
    coefRMSE_sinu = []
    coefDIFR_sinu = []
    # penasblancas Q
    coefNS_peba   = []
    coefRMSE_peba = []
    coefDIFR_peba = []
    # regidor Q
    coefNS_regi   = []
    coefRMSE_regi = []
    coefDIFR_regi = []
    
    # Llenado de datos NS
    coefNS_pube.append(-999999)
    coefNS_peba.append(-999999)
    coefNS_barr.append(-999999)
    coefNS_puwi.append(-999999)
    coefNS_sapa.append(-999999)
    coefNS_sinu.append(-999999)
    coefNS_badi.append(-999999)
    coefNS_elco.append(-999999)
    coefNS_lagl.append(-999999)
    coefNS_regi.append(-999999)
    coefNS_peno.append(-999999)
    
    coefRMSE_pube.append(999999)
    coefRMSE_peba.append(999999)
    coefRMSE_barr.append(999999)
    coefRMSE_puwi.append(999999)
    coefRMSE_sapa.append(999999)
    coefRMSE_sinu.append(999999)
    coefRMSE_badi.append(999999)
    coefRMSE_elco.append(999999)
    coefRMSE_lagl.append(999999)
    coefRMSE_regi.append(999999)
    coefRMSE_peno.append(999999)
    
    coefDIFR_pube.append(999999)
    coefDIFR_peba.append(999999)
    coefDIFR_barr.append(999999)
    coefDIFR_puwi.append(999999)
    coefDIFR_sapa.append(999999)
    coefDIFR_sinu.append(999999)
    coefDIFR_badi.append(999999)
    coefDIFR_elco.append(999999)
    coefDIFR_lagl.append(999999)
    coefDIFR_regi.append(999999)
    coefDIFR_peno.append(999999)
    
    print('Upss, algo ha sucedido')

# print resultados
result_ns   = []
result_RMSE = []
result_DIFR = []

result_ns.append(1 - coefNS_pube[0])
result_ns.append(1 - coefNS_peba[0])
result_ns.append(1 - coefNS_barr[0])
result_ns.append(1 - coefNS_puwi[0])
result_ns.append(1 - coefNS_sapa[0])
result_ns.append(1 - coefNS_sinu[0])
result_ns.append(1 - coefNS_badi[0])
result_ns.append(1 - coefNS_elco[0])
result_ns.append(1 - coefNS_lagl[0])
result_ns.append(1 - coefNS_regi[0])
result_ns.append(1 - coefNS_peno[0])

result_RMSE.append(coefRMSE_pube[0])
result_RMSE.append(coefRMSE_peba[0])
result_RMSE.append(coefRMSE_barr[0])
result_RMSE.append(coefRMSE_puwi[0])
result_RMSE.append(coefRMSE_sapa[0])
result_RMSE.append(coefRMSE_sinu[0])
result_RMSE.append(coefRMSE_badi[0])
result_RMSE.append(coefRMSE_elco[0])
result_RMSE.append(coefRMSE_lagl[0])
result_RMSE.append(coefRMSE_regi[0])
result_RMSE.append(coefRMSE_peno[0])

result_DIFR.append(coefDIFR_pube[0])
result_DIFR.append(coefDIFR_peba[0])
result_DIFR.append(coefDIFR_barr[0])
result_DIFR.append(coefDIFR_puwi[0])
result_DIFR.append(coefDIFR_sapa[0])
result_DIFR.append(coefDIFR_sinu[0])
result_DIFR.append(coefDIFR_badi[0])
result_DIFR.append(coefDIFR_elco[0])
result_DIFR.append(coefDIFR_lagl[0])
result_DIFR.append(coefDIFR_regi[0])
result_DIFR.append(coefDIFR_peno[0])

# Export results
result_df = pd.DataFrame()
result_df['NS'] = result_ns

result_df_0 = pd.DataFrame()
result_df_0 ['RMSE'] = result_RMSE
result_df_0 ['DIFR'] = result_DIFR

os.chdir(p_work)
os.chdir('./RESULTS')

result_df.to_csv('NS_results.dat',index = False)

# Print results
#print(strikler)
#print(result_df)
#print(result_df_0)
#
#import matplotlib.pyplot as plt
#
#plt.plot(mod_z_pube, '.-', label = 'mod')
#plt.legend()
#plt.title(coefNS_pube)
#plt.grid()
#plt.show()
#
#plt.plot(obs_z_pube, '.-', label = 'obs')
#plt.legend()
#plt.title(coefNS_pube)
#plt.grid()
#plt.show()
#
#plt.plot(np.abs(np.array(mod_z_pube) - np.array(obs_z_pube)), label = 'd pube - 1')
#plt.plot(np.abs(np.array(mod_z_barr) - np.array(obs_z_barr)), label = 'd barr - 2')
#plt.plot(np.abs(np.array(mod_z_puwi) - np.array(obs_z_puwi)), label = 'd puwi - 3')
#plt.plot(np.abs(np.array(mod_z_sapa) - np.array(obs_z_sapa)), label = 'd sapa - 4')
#plt.plot(np.abs(np.array(mod_z_sinu) - np.array(obs_z_sinu)), label = 'd sinu - 5')
#plt.plot(np.abs(np.array(mod_z_badi) - np.array(obs_z_badi)), label = 'd badi - 6')
#plt.plot(np.abs(np.array(mod_z_elco) - np.array(obs_z_elco)), label = 'd elco - 7')
#plt.plot(np.abs(np.array(mod_z_lagl) - np.array(obs_z_lagl)), label = 'd lagl - 8')
#plt.plot(np.abs(np.array(mod_z_peno) - np.array(obs_z_peno)), label = 'd peno - 9')
#plt.title('Diferencia entre nivel observado y nivel modelado')
#plt.xlabel('Day')
#plt.ylabel('Delta m')
#plt.legend()
#plt.grid()
#plt.show()
