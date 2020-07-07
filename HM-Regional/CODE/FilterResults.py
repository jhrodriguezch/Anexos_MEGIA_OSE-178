# -*- coding: utf-8 -*-
"""
Universidad NAcional sede Bogota
Elaborado por: Manuel Mejía y Jhonatan Rodríguez

Obj: Lectura de los resultados del modelo MASCARET para el proyecto MEGIA
"""

import numpy as np
import pandas as pd

def FilterResults(file_name, variable):
    
    # Variable a extraer - X, Z, Zref, Q
    input_file = open(file_name + '_NEST.lis','r')
    
    ptp = False
    timeLine = 0
    
    df_Z = pd.DataFrame()
    df_Z_2 = pd.DataFrame()
    
    df_Q = pd.DataFrame()
    df_Q_2 = pd.DataFrame()
    count = 0
    
    for cnt, line in enumerate(input_file):
        if "RESULTATS DU MODELE MASCAR EN NP =" in line: 
            ptp = True
            timeLine = cnt
            
            # Para los nombres de las columnas
            t = float(line[50:-1])
            jour = int(t/(86400))
            heure = int((t/86400 - jour) * 24)
            minute = int((((t/86400 - jour) * 24) - heure) * 60)
            seconde = int((((((t/86400 - jour) * 24) - heure) * 60) - minute) * 60)
            
            # Comenzar los valores
            X = []
            Q = []
            Z = []
            Zref = []
        elif "=======================================================================================" in line: 
            try:
                # Guardar los valores importantes
                # Valor 1 - list X
                if variable == 'x':
                    X = [item for item in X if item]
                    X = list(np.double(X[1:]))
                    break
                # Valor 2 - dataframe Q
                if variable == 'z' or variable == 'q':
                    Q = [item for item in Q if item]             
                    Q = list(np.double(Q[1:]))
                    Z = [item for item in Z if item]
                    Z = list(np.double(Z[1:]))        
                
                #Valor 4 - list Zref
                if variable == 'zref':
                    Zref = [item for item in Zref if item]
                    Zref = list(np.double(Zref[1:]))      
                    break
                #Nombre columna dataframe  
                col_name = 3 * ' ' + str(jour) + 3 * ' ' + str(heure) + 3 * ' ' + str(minute) + 3 * ' ' + str(seconde)
                
                # Creacion dataframes
                if variable == 'z' or variable == 'q':
                 
                    if jour == count:
                        df_Z_2 [col_name] = Z
                        df_Q_2 [col_name] = Q
                        
                    else:
                        df_Z[str(count)] = list(df_Z_2.mean(axis = 1).values)
                        df_Z_2 = pd.DataFrame()
                        df_Z_2[col_name] = Z
                        
                        df_Q[str(count)] = list(df_Q_2.mean(axis = 1).values)
                        df_Q_2 = pd.DataFrame()
                        df_Q_2[col_name] = Q
                        count = jour
                               
                ptp = False
            except:
                ptp = False
        elif 'TS CALCUL' in line:
            # Guardar los valores importantes
            # Valor 1 - list X
            if variable == 'x':
                X = [item for item in X if item]
                X = list(np.double(X[1:]))
            
            # Valor 2 - DataFrame Q
            if variable == 'z' or variable == 'q':
                Q = [item for item in Q if item]
                Q = list(np.double(Q[1:]))
            
                Z = [item for item in Z if item]
                Z = list(np.double(Z[1:]))        
            
            #Valor 4 - list Zref
            if variable == 'zref':
                Zref = [item for item in Zref if item]
                Zref = list(np.double(Zref[1:]))          
            
            #Nombre columna dataframe  
            col_name = 3 * ' ' + str(jour) + 3 * ' ' + str(heure) + 3 * ' ' + str(minute) + 3 * ' ' + str(seconde)
            
            # Creacion dataframes
            if variable == 'z' or variable == 'q':
                
                if jour == count:
                    df_Z_2 [col_name] = Z
                    df_Q_2 [col_name] = Q
                else:
                    df_Z[str(count)] = list(df_Z_2.mean(axis = 1).values)
                    df_Z_2 = pd.DataFrame()
                    df_Z_2[col_name] = Z
                    
                    df_Q[str(count)] = list(df_Q_2.mean(axis = 1).values)
                    df_Q_2 = pd.DataFrame()
                    df_Q_2[col_name] = Q
                    count = jour
                
            
            ptp = False
        elif cnt > timeLine+11 and ptp:
            # Columnas que se requieren sacar de la cadena            

            if variable == 'x':
                X.append(line[5: 16])
            if variable == 'zref':
                Zref.append(line[17: 25])
            if variable == 'z' or variable == 'q':
                Q.append(line[-9: -1])
                Z.append(line[26: 35])

    if variable == 'z' or variable == 'q':
        df_Z[str(count)] = list(df_Z_2.mean(axis = 1).values)
        df_Q[str(count)] = list(df_Q_2.mean(axis = 1).values)

        
    input_file.close()
    return(X, Zref, df_Z, [], [], [], [], [], df_Q)

#a = 'MEGIA'
#variable = 'q'
#X, Zref, df_Z, b, b, b, b, b, df_Q = FilterResults(a, variable)