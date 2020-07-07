#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:50:15 2019
@Obj: A partir de .rub, archivo donde se encuentra la solucion generada por 
MASCARET, obteneer la serie de datos de manera clasica para observación de los 
resultados y creacion de futuros archivos
@author: jhonatan RODRIGUEZ
@project: MEGIA

"""

# librerias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Otros
def fila2vector(fila, n):
    # fila es la cadena de caracteries que continen los numero a trabajar
    # n es el separador usado en la cadena de caracteres para separar los numeros
    number =""
    result = []
    for i in fila:
        if i != n:
            number = number + i
        else:
            if number != "":
                result.append(number)
            number = ""
    result.append(number)
    return(result)

def main_function_sol2serie (file_name):
    # PROGRAMA
    #file_name = "SEC_FULL_TRPZ.rub"
    file1 = open(file_name)
    print('---')
    
    #  Lee el archivo y lo coloca en una serie de tiempo
    df = []
    for c1 in file1.readlines():
        fila = str(c1)
        df.append(fila.strip())
    file1.close()
    
    # crear vector con los datos calculados
    result_2p = []
    vector_2p_sol = ['first_value']
    dt_solucion = []
    trsh = 0
    
    for c2 in np.arange(5,len(df)):
        fila = df[c2]
        fila = fila.replace(" ", "+")
        vector = fila2vector(fila, "+")
        result_2p.append(vector)
        if len(vector) == 1 and vector[0] != 'FIN' and vector[0] != '-----------------------------------------------------------------------':
            #print('------------------------------------------------')
            #print(vector_2p_sol)
            try:
                #print(float(vector[0]))
                vector_2p_sol.append(float(vector[0]))
            except:
                
                try:
                    if vector_2p_sol[0] != 'first_value':
                        # Plotea los resultados obtenidos de MASCARET
                        #print(vector_2p_sol[0])
                        dt_solucion.append(str(vector_2p_sol[0]))
                        dt_solucion.append(vector_2p_sol[1:])
                        #plt.plot(vector_2p_sol[1:], '.')
                        #plt.show()
                        #DT_solucion [str(j)] = vector_2p_sol[1:]
                    vector_2p_sol = []
                    vector_2p_sol.append(vector[0])
                except:
                    trsh = 0
    
        else:
            for c22 in vector:
                try:
                    #print(float(c22))
                    vector_2p_sol.append(float(c22))
                except:
                    trsh = 0
    print('----')
    
    # Crear el dataframe
    DT_solution = pd.DataFrame()
    m = 0
    for i in np.arange(0, len(dt_solucion)):
        if i % 2 == 0:
            col_name = str(dt_solucion[i])+' ' +str(m)
            m += 1
            #print(col_name)
        else:
            try:
                DT_solution[col_name] = dt_solucion[i]
                # La cantidad de variableas va hasta diea
            except:
                trsh = 0
    print('----')
    return(DT_solution)

#file_name = "SEC_FULL_TRPZ.rub"
#sol = main_function_sol2serie (file_name)


# Combierte archivo .rub en dataframe
