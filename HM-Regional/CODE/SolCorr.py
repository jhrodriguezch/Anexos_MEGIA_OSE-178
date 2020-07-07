#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:30:34 2019

@author: girehe2o
Requiere soldf, producto de MainMASCARET1D
"""
# librerias
import numpy as np

def main_function_seriecorr (soldf):
    temp = 0
    name_columns_vector = []
    for i in soldf.columns:
        if i[0] == 'X':
            temp += 1
        name_col = ''
        for j in np.arange(0,len(i)):
            m = i.strip()
            if m[j] == " ":
                break
            name_col = name_col + m[j]
            #print(m[j])
        name_columns_vector.append(name_col + " " + str(temp))
        #print(name_col, temp)
    #soldf.rename(name_columns_vector)
    #print(name_columns_vector)
    soldf.columns = name_columns_vector
    return(soldf, temp)