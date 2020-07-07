#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:56:05 2019
Nombre: soldf2lig
@author: girehe2o
Obj: Generar a partir de un dataframe determinado un archivo .lig, condiciones 
iniciales para el modelo MASCARET

Requiere
Libreria os
- soldf -> corregido
- N_paso
"""
import pandas as pd

from Sol2Serie import *
from SolCorr import *

def serie2line(df_data):
    line = ""
    j = 0
    for i in df_data:
        line +=  (13-len(str(i)))*" " + str(i)
        j += 1
#        if j > 73:
#            break
    line += '\n'
    return(line, j)
    
# Main archivo
def soldf2lig(soldf, N_paso, file_name):
    Nuevo_arch = file_name+"_NEST.lig"
    
    cad_1 = 'X '+str(N_paso)
    cad_2 = 'Z '+str(N_paso)
    cad_3 = 'QMIN '+str(N_paso)
    
    x_value = soldf[cad_1]
    z_value = soldf[cad_2]
    q_value = soldf[cad_3]
    
    x_value = [int(x) for x in x_value]
    z_value = [round(z,2) for z in z_value]
    q_value = [round(q,2) for q in q_value]
    
    # temoporal
    #x_value_t = [0,	2400,	3200,	3600,	5200,	12400,	12800,	16800,	18400,	23600,	31600,	34800,	35200,	35600,	48800,	56000,	62000,	62800,	64800,	69200,	70400,	70800,	74800,	75200,	84000,	84400,	84800,	89200,	89600,	96000,	96800,	97200,	97600,	100800,	102400,	103600,	105600,	107200,	115200,	115600,	116800,	122800,	129200,	135200,	150400,	152400,	152800,	164000,	174800,	186000,	186400,	188000,	188400,	188800,	194400,	194800,	196800,	197200,	198800,	211600,	246400,	252400,	257600,	258000,	266400,	272800,	298400,	304400,	317200,	317600,	322400,	322800,	325600,	362000]
    #x_value = pd.Series ()
    #x_value = x_value_t
    
    x_line, val_total = serie2line(x_value)
    z_line, val_total = serie2line(z_value)
    q_line, val_total = serie2line(q_value)
    
    file = open(Nuevo_arch, "w")
    file.write('RESULTATS CALCUL,DATE :  00/00/00 00:00\n')
    file.write('FICHIER RESULTAT MASCARET  \n')
    file.write('----------------------------------------------------------------------- \n')
    file.write(' IMAX  =')
    file.write((5 - len(str(val_total))) * ' ' + str(int(val_total)))
    file.write(' NBBIEF=    1\n')
    file.write(' I1,I2 =    1    ')
    file.write(str(int(val_total)))
    file.write('\n')
    file.write(' X\n')
    file.write(x_line)
    file.write(' Z\n')
    file.write(z_line)
    file.write(' Q\n')
    file.write(q_line)
    file.write(' FIN\n')
    file.close()
    return (True)