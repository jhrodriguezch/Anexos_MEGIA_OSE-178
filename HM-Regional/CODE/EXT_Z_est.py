#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:08:46 2019

@author: IC Jhonatan Rodriguez
Nombre código: EXT_Z_est
Obj: Estraer los datos de la matriz Z generado por el codigo MainMASCARET1D

"""
# Librerias
import numpy as np

#nombre = 'barrancabermeja'
#codigo = 23157030
#abz = 109054.3914


def EXT_Z_est(abz, X, Z):
    
    
    X = np.array(X)
    
    # Extraccion de puntos vecinos
    X_back = max(X[(X - abz) <= 0])
    X_up = min(X[(X - abz) >= 0])
    
    if X_back != X_up: 
    
        Z_back = Z[X == max(X[(X - abz) <= 0])].copy()
        Z_back = Z_back.reset_index()
        Z_up = Z[X == min(X[(X - abz) >= 0])].copy()
        Z_up = Z_up.reset_index()
        
        # Interpolación lineal
        Z_in = (((Z_back - Z_up) / (X_back - X_up)) * (abz - X_back)) + Z_back
    else:
        Z_in = Z[X == abz].copy()
        Z_in = Z_in.reset_index()

    return(Z_in)