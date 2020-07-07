#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:54:19 2019

@author: jhrodriguezch
obj: crear los archivos .xcas para el modelo MASCARET a partir de los valores de
strikler y los caudales desconocidos
Opciones:
    i = 1 : Crear el archivo para modelo en estado estacionario
    i = 2 : Crear el archivo para modelo en estado no estacionario
    i = 3 : Prueba
"""
# Librerias
import numpy as np

# Valores iniciales
#XCAS_new = 'prb2.xcas'
#i = 1
#abz_cort = [0, 90838, 125686, 140069, 176823, 198248, 230469, 237946, 276599, 283232, 362000] #Valor de abscisado
#coef_Strk = [27.03, 27.78, 32.26, 33.33, 33.33, 33.33, 33.33, 33.33, 25.81, 25.81]

def crearXCAS(XCAS_new, i, abz_cort, coef_Strk):
    # vector2str
    abz_cor_1 = ''
    abz_cor_2 = ''
    Strk_str = ''
    
    for j in np.arange(len(abz_cort)-1):
        abz_cor_1 += str('%.0f' % abz_cort[j]) + ' '
        abz_cor_2 += str('%.0f' % abz_cort[j + 1]) + ' '
        Strk_str += str('%.2f' % coef_Strk[j]) + ' '
        
    
    # Creacion del archivo
    file = open(XCAS_new, 'w')
    
    file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
    file.write('<!DOCTYPE fichierCas SYSTEM "mascaret-1.0.dtd">\n')
    file.write('<fichierCas>\n')
    file.write('  <parametresCas>\n')
    file.write('    <parametresGeneraux>\n')
    file.write('      <versionCode>3</versionCode>\n')
    
    if i == 1:
        file.write('      <code>1</code>\n')
    if i == 2:
        file.write('      <code>3</code>\n')
        
    if i == 1:
        file.write('      <fichMotsCles>MEGIA_EST_PRB.xcas</fichMotsCles>\n')
    if i == 2:
        file.write('      <fichMotsCles>MEGIA_NEST_PRB.xcas</fichMotsCles>\n')
    
    file.write('      <dictionaire>dico.txt</dictionaire>\n')
    file.write('      <progPrincipal>princi.f</progPrincipal>\n')
    file.write('      <sauveModele>false</sauveModele>\n')
    
    if i == 1:
        file.write('      <fichSauvModele>MEGIA_EST.tmp</fichSauvModele>\n')
    if i == 2:
        file.write('      <fichSauvModele>MEGIA_NEST.tmp</fichSauvModele>\n')
    
    file.write('      <validationCode>false</validationCode>\n')
    file.write('      <typeValidation>1</typeValidation>\n')
    file.write('      <presenceCasiers>false</presenceCasiers>\n')
    file.write('      <bibliotheques>\n')
    file.write('        <bibliotheque>mascaretV5P1.a damoV3P0.a</bibliotheque>\n')
    file.write('      </bibliotheques>\n')
    file.write('    </parametresGeneraux>\n')
    file.write('    <parametresModelePhysique>\n')
    file.write('      <perteChargeConf>false</perteChargeConf>\n')
    file.write('      <compositionLits>2</compositionLits>\n')
    file.write('      <conservFrotVertical>false</conservFrotVertical>\n')
    file.write('      <elevCoteArrivFront>0.05</elevCoteArrivFront>\n')
    file.write('      <interpolLinStrickler>false</interpolLinStrickler>\n')
    file.write('      <debordement>\n')
    file.write('        <litMajeur>false</litMajeur>\n')
    file.write('        <zoneStock>false</zoneStock>\n')
    file.write('      </debordement>\n')
    file.write('    </parametresModelePhysique>\n')
    file.write('    <parametresNumeriques>\n')
    file.write('      <calcOndeSubmersion>false</calcOndeSubmersion>\n')
    file.write('      <froudeLimCondLim>1000.0</froudeLimCondLim>\n')
    file.write('      <traitImplicitFrot>false</traitImplicitFrot>\n')
    file.write('      <hauteurEauMini>0.005</hauteurEauMini>\n')
    file.write('      <implicitNoyauTrans>false</implicitNoyauTrans>\n')
    file.write('      <optimisNoyauTrans>false</optimisNoyauTrans>\n')
    file.write('      <perteChargeAutoElargissement>false</perteChargeAutoElargissement>\n')
    file.write('      <termesNonHydrostatiques>false</termesNonHydrostatiques>\n')
    file.write('      <apportDebit>0</apportDebit>\n')
    file.write('      <attenuationConvection>false</attenuationConvection>\n')
    file.write('    </parametresNumeriques>\n')
    file.write('    <parametresTemporels>\n')
    
# Parámetros temporales
    if i == 1:    
        file.write('      <pasTemps>200000.0</pasTemps>\n')
        file.write('      <tempsInit>0.0</tempsInit>\n')
        file.write('      <critereArret>2</critereArret>\n')# 2 Numero de pasos de tiempo máximos
        file.write('      <nbPasTemps>3</nbPasTemps>\n')
        file.write('      <tempsMax>1.0</tempsMax>\n')
        file.write('      <pasTempsVar>false</pasTempsVar>\n')
        file.write('      <nbCourant>0.8</nbCourant>\n')
        file.write('      <coteMax>0.0</coteMax>\n')
        file.write('      <abscisseControle>0.0</abscisseControle>\n')
        file.write('      <biefControle>1</biefControle>\n')
    elif i == 2:      
        file.write('      <pasTemps>3600.0</pasTemps>\n')
        file.write('      <tempsInit>0.0</tempsInit>\n')
        file.write('      <critereArret>2</critereArret>\n')
        #file.write('      <nbPasTemps>60000</nbPasTemps>\n')
        file.write('      <nbPasTemps>3000000</nbPasTemps>\n')
        # CALIBRACION = pastemps = 3600.0 t nbpasTemps = 2700000 son 115 d de 
        # modelacion dx = 100
        file.write('      <tempsMax>1.0</tempsMax>\n')
        file.write('      <pasTempsVar>true</pasTempsVar>\n')
        file.write('      <nbCourant>0.8</nbCourant>\n')
        file.write('      <coteMax>0.0</coteMax>\n')
        file.write('      <abscisseControle>0.0</abscisseControle>\n')
        file.write('      <biefControle>1</biefControle>\n')
          
    file.write('    </parametresTemporels>\n')
    file.write('    <parametresGeometrieReseau>\n')
    file.write('      <geometrie>\n')
    file.write('        <fichier>SEC_COR_TRPZ.geo</fichier>\n')
    file.write('        <format>2</format>\n')
    file.write('        <profilsAbscAbsolu>false</profilsAbscAbsolu>\n')
    file.write('      </geometrie>\n')
    file.write('      <listeBranches>\n')
    file.write('        <nb>1</nb>\n')
    file.write('        <numeros>1</numeros>\n')
    file.write('        <abscDebut>0.0</abscDebut>\n')
    file.write('        <abscFin>362000.0</abscFin>\n')
    file.write('        <numExtremDebut>1</numExtremDebut>\n')
    file.write('        <numExtremFin>74</numExtremFin>\n')
    file.write('      </listeBranches>\n')
    file.write('      <listeNoeuds>\n')
    file.write('        <nb>0</nb>\n')
    file.write('        <noeuds/>\n')
    file.write('      </listeNoeuds>\n')
    
    # Extremos libres, entrada y salidad del modelo
    file.write('      <extrLibres>\n')
    file.write('        <nb>2</nb>\n')
    file.write('        <num>1 2</num>\n')
    file.write('        <numExtrem>1 74</numExtrem>\n')
    file.write('        <noms>\n')
    file.write('          <string>limite1</string>\n')
    file.write('          <string>limite2</string>\n')
    file.write('        </noms>\n')
    file.write('        <typeCond>1 2</typeCond>\n')
    #   Seleccion del .loi correspondiente
    file.write('        <numLoi>1 4</numLoi>\n')
    file.write('      </extrLibres>\n')
    
    file.write('    </parametresGeometrieReseau>\n')
    file.write('    <parametresConfluents>\n')
    file.write('      <nbConfluents>0</nbConfluents>\n')
    file.write('      <confluents/>\n')
    file.write('    </parametresConfluents>\n')
    file.write('    <parametresPlanimetrageMaillage>\n')
    file.write('      <methodeMaillage>5</methodeMaillage>\n')
    file.write('      <planim>\n')
    
    # !!! Discretización vertical de la sección transversal
    file.write('        <nbPas>50</nbPas>\n')
    file.write('        <nbZones>1</nbZones>\n')
    file.write('        <valeursPas>0.5</valeursPas>\n')
    
    file.write('        <num1erProf>1</num1erProf>\n')
    file.write('        <numDerProf>74</numDerProf>\n')
    file.write('      </planim>\n')
    file.write('      <maillage>\n')
    file.write('        <modeSaisie>2</modeSaisie>\n')
    file.write('        <sauvMaillage>true</sauvMaillage>\n')
    file.write('        <maillageClavier>\n')
    file.write('          <nbSections>0</nbSections>\n')
    file.write('          <nbPlages>1</nbPlages>\n')
    file.write('          <num1erProfPlage>1</num1erProfPlage>\n')
    file.write('          <numDerProfPlage>74</numDerProfPlage>\n')
# Parámetros espaciales
    file.write('          <pasEspacePlage>100.0</pasEspacePlage>\n')
    
    file.write('          <nbZones>0</nbZones>\n')
    file.write('        </maillageClavier>\n')
    file.write('      </maillage>\n')
    file.write('    </parametresPlanimetrageMaillage>\n')
    file.write('    <parametresSingularite>\n')
    file.write('      <nbSeuils>0</nbSeuils>\n')
    file.write('    </parametresSingularite>\n')
    file.write('    <parametresApportDeversoirs>\n')
    file.write('      <debitsApports>\n')
    file.write('        <nbQApport>19</nbQApport>\n')
    file.write('        <noms>\n')
    file.write('          <string>SAN_BARTOLOME</string>\n')
    file.write('          <string>RIO_CARARE</string>\n')
    file.write('          <string>RIO_OPON</string>\n')
    file.write('		  <string>BRA_ROMPIDA</string>\n')
    file.write('          <string>RIO_SOGAMOSO</string>\n')
    file.write('          <string>RIO_CIMITARRA</string>\n')
    file.write('		  <string>BRA_SIMITI</string>\n')
    file.write('		  <string>BRA_MORALES_O</string>\n')
    file.write('          <string>RIO_LEBRIJA</string>\n')
    file.write('		  <string>BRA_MORALES_I</string>\n')
    # CIENAGAS  16/06/2020
    file.write('		  <string>CIENAGA_34100</string>\n')
    file.write('		  <string>CIENAGA_42400</string>\n')
    file.write('		  <string>CIENAGA_161500</string>\n')
    file.write('		  <string>CIENAGA_168400</string>\n')
    file.write('		  <string>CIENAGA_255100</string>\n')
    file.write('		  <string>CIENAGA_278500</string>\n')
    file.write('		  <string>CIENAGA_305100</string>\n')
    file.write('		  <string>CIENAGA_307400</string>\n')
    file.write('		  <string>CIENAGA_341500</string>\n')
    
    file.write('        </noms>\n')
    file.write('        <numBranche>1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1</numBranche>\n')
    file.write('        <abscisses>18497.0 58156.0 103793.0 108943.0 121345.0 138605.0 154777.0 220334.0 247553.0 308582.0 34100.0 42400.0 161500.0 168400.0 255100.0 278500.0 305100.0 307400.0 341500.0</abscisses>\n')
    file.write('        <longueurs>0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0</longueurs>\n')
    file.write('        <numLoi>5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23</numLoi>\n')
    file.write('      </debitsApports>\n')
    file.write('    </parametresApportDeversoirs>\n')
    file.write('    <parametresCalage>\n')
    file.write('      <frottement>\n')
    file.write('        <loi>1</loi>\n')
    file.write('        <nbZone>10</nbZone>\n')
    file.write('        <numBranche>1 1 1 1 1 1 1 1 1 1</numBranche>\n')
            
    file.write('        <absDebZone>')
    #file.write('0.0 90838.0 125686.0 140069.0 176823.0 198248.0 230469.0 237946.0 276599.0 283232.0')
    file.write(abz_cor_1)
    
    file.write('</absDebZone>\n')
    file.write('        <absFinZone>')
    
    #file.write('90838.0 125686.0 140069.0 176823.0 198248.0 230469.0 237946.0 276599.0 283232.0 362000.0')
    file.write(abz_cor_2)
    
    file.write('</absFinZone>\n')
    file.write('        <coefLitMin>')
    
    #file.write('27.03 27.78 32.26 33.33 33.33 33.33 33.33 33.33 25.81 25.81')
    file.write(Strk_str.strip())
    
    file.write('</coefLitMin>\n')
    file.write('        <coefLitMaj>')
    
    #file.write('27.03 27.78 32.26 33.33 33.33 33.33 33.33 33.33 25.81 25.81')
    file.write(Strk_str.strip())
    
    file.write('</coefLitMaj>\n')
    
    file.write('      </frottement>\n')
    file.write('      <zoneStockage>\n')
    file.write('        <nbProfils>0</nbProfils>\n')
    file.write('        <numProfil>-0</numProfil>\n')
    file.write('        <limGauchLitMaj>-0</limGauchLitMaj>\n')
    file.write('        <limDroitLitMaj>-0</limDroitLitMaj>\n')
    file.write('      </zoneStockage>\n')
    file.write('    </parametresCalage>\n')
    file.write('    <parametresLoisHydrauliques>\n')
    
    # Numero .loi's que se leen
    file.write('      <nb>23</nb>\n')
    file.write('      <lois>\n')
    
    # Entrada del modelo, Caudal aguas arriba, Caudal Puerto Berrio
    # loi 1
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>Q_PUERTOBERRIO</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_QMD_23097030_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')

    if i == 2:
        #loi 1 ---- Condiciones de caudal del año 2013
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>Q_PUERTOBERRIO</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_QMD_23097030.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')   
    
    # loi 2 - Condicion cienaga 1 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>N_16012013_PTE_BERRIO</nom>\n')
    file.write('          <type>2</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>SEC_FULL_m_1.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # loi 3 - Condicion cienaga 2 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>Q_19012013_PENONSITO</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>SEC_FULL_m_2.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # loi 4
    # Condiciones iniciales aguas abajo, estacion Penonsito, Nivel
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>N_25027330_PENONSITO</nom>\n')
        file.write('          <type>2</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_C_NVD_25027330_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>N_25027330_PENONSITO</nom>\n')
        file.write('          <type>2</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_C_NVD_25027330.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')        
    
    # Entradas fijas --(Hidrologia)
    # Con desembocadura determinada

    # Río SAN BARTOLOME 
    # loi 5 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>RIO_SAN_BARTOLOME</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>Q_R_SANBARTOLOME.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # Río CARARE
    # loi 6 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>RIO_CARARE</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>Q_R_CARARE.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # Río OPON
    # loi 7
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_OPON</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_OPON_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_OPON</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_OPON.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    
    # Brazo ROMPIDA
    # loi 8 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>BRA_ROMPIDA</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>Q_B_ROMPIDA.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # Río SOGAMOSO
    # loi 9
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_SOGAMOSO</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_SOGAMOSO_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_SOGAMOSO</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_SOGAMOSO.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
        
    # Río CIMITARRA
    # loi 10
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_CIMITARRA</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_CIMITARRA_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_CIMITARRA</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_CIMITARRA.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    
    # BRAZO SIMITI
    # loi 11 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>BRA_SIMITI</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>Q_B_SIMITI.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # BRAZO MORALES O
    # loi 12 # UNUSED
    file.write('        <structureParametresLoi>\n')
    file.write('          <nom>BRA_MORALES_O</nom>\n')
    file.write('          <type>1</type>\n')
    file.write('          <donnees>\n')
    file.write('            <modeEntree>1</modeEntree>\n')
    file.write('            <fichier>Q_B_MORALESO.loi</fichier>\n')
    file.write('            <uniteTps>-0</uniteTps>\n')
    file.write('            <nbPoints>-0</nbPoints>\n')
    file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
    file.write('          </donnees>\n')
    file.write('        </structureParametresLoi>\n')
    
    # Río LEBRIJA
    # loi 13
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_LEBRIJA</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_LEBRIJA_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>RIO_LEBRIJA</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_LEBRIJA.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    
    # BRAZO MORALES I
    # loi 14
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>BRA_MORALES_I</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_MORALESI_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>BRA_MORALES_I</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_R_MORALESI.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    
    # loi 15 - C. 34100
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_34100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_34100_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_34100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_34100.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
        
    # loi 16 - C. 42400
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_42400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_42400_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_42400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_42400.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')    
    
    # loi 17 - C. 161500
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_161500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_161500_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_161500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_161500.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')      
    
    # loi 18 - C. 168400
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_168400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_168400_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_168400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_168400.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')   

    # loi 19 - C. 255100
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_255100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_255100_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_255100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_255100.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')       
    
    # loi 20 - C. 278500
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_278500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_278500_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_278500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_278500.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')          
    
    # loi 21 - C. 305100
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_305100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_305100_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_305100</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_305100.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')       
    
    # loi 22 - C. 307400
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_307400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_307400_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_307400</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_307400.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')        
    
    # loi 23 - C. 341500
    if i == 1:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_341500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_341500_cal.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')
    if i == 2:
        file.write('        <structureParametresLoi>\n')
        file.write('          <nom>CIENAGA_341500</nom>\n')
        file.write('          <type>1</type>\n')
        file.write('          <donnees>\n')
        file.write('            <modeEntree>1</modeEntree>\n')
        file.write('            <fichier>Q_C_341500.loi</fichier>\n')
        file.write('            <uniteTps>-0</uniteTps>\n')
        file.write('            <nbPoints>-0</nbPoints>\n')
        file.write('            <nbDebitsDifferents>-0</nbDebitsDifferents>\n')
        file.write('          </donnees>\n')
        file.write('        </structureParametresLoi>\n')    
    
    file.write('      </lois>\n')
    
    # Entradas dinámicas -- (Hidrogeología)
    # Dependen de la altura del nivel freatico. Cambia en cada punto del río
    # ------------------------ Falta incluirlo --------------------------------
    
    file.write('    </parametresLoisHydrauliques>\n')
    file.write('    <parametresConditionsInitiales>\n')
    file.write('      <repriseEtude>\n')
    file.write('        <repriseCalcul>false</repriseCalcul>\n')
    file.write('      </repriseEtude>\n')
    file.write('      <ligneEau>\n')
    if i == 1:      
        file.write('        <LigEauInit>false</LigEauInit>\n')
        file.write('        <modeEntree>2</modeEntree>\n')
        file.write('        <formatFichLig>1</formatFichLig>\n')
        file.write('        <nbPts>0</nbPts>\n')
        file.write('        <branche>-0</branche>\n')
        file.write('        <abscisse>-0</abscisse>\n')
        file.write('        <cote>-0</cote>\n')
        file.write('        <debit>-0</debit>\n')
    if i == 2:        
        file.write('        <LigEauInit>true</LigEauInit>\n')
        file.write('        <modeEntree>1</modeEntree>\n')
        file.write('        <fichLigEau>MEGIA_NEST.lig</fichLigEau>\n')
        file.write('        <formatFichLig>2</formatFichLig>\n')
        file.write('        <nbPts>-0</nbPts>\n')
            
    file.write('      </ligneEau>\n')
    file.write('    </parametresConditionsInitiales>\n')
    file.write('    <parametresImpressionResultats>\n')
    
    if i == 1:
        file.write('      <titreCalcul>Estudio Hidrodinámico MEGIA - Regional - Estacionario</titreCalcul>\n')
    if i == 2:
        file.write('      <titreCalcul>Estudio Hidrodinámico MEGIA - Regional - No Estacionario</titreCalcul>\n')
    file.write('      <impression>\n')
    file.write('        <impressionGeometrie>false</impressionGeometrie>\n')
    file.write('        <impressionPlanimetrage>true</impressionPlanimetrage>\n')
    file.write('        <impressionReseau>false</impressionReseau>\n')
    file.write('        <impressionLoiHydraulique>false</impressionLoiHydraulique>\n')
    file.write('        <impressionligneEauInitiale>false</impressionligneEauInitiale>\n')
    file.write('        <impressionCalcul>true</impressionCalcul>\n')
    file.write('      </impression>\n')
    file.write('      <pasStockage>\n')
    file.write('        <premPasTpsStock>1</premPasTpsStock>\n')
    file.write('        <pasStock>1</pasStock>\n')
    file.write('        <pasImpression>5</pasImpression>\n')
    file.write('      </pasStockage>\n')
    file.write('      <resultats>\n')
    if i == 1:      
        file.write('        <fichResultat>MEGIA_EST.rub</fichResultat>\n')
    if i == 2:
        file.write('        <fichResultat>MEGIA_NEST.rub</fichResultat>\n')
            
    file.write('        <postProcesseur>1</postProcesseur>\n')
    file.write('      </resultats>\n')
    file.write('      <listing>\n')
    
    if i == 1:      
        file.write('        <fichListing>MEGIA_EST.lis</fichListing>\n')
    if i == 2:
        file.write('        <fichListing>MEGIA_NEST.lis</fichListing>\n')
            
    file.write('      </listing>\n')
    file.write('      <fichReprise>\n')
    if i == 1:      
        file.write('        <fichRepriseEcr>MEGIA_EST.rep</fichRepriseEcr>\n')
    if i == 2:
        file.write('        <fichRepriseEcr>MEGIA_NEST.rep</fichRepriseEcr>\n')
            
    file.write('      </fichReprise>\n')
    file.write('      <rubens>\n')
    file.write('        <ecartInterBranch>1.0</ecartInterBranch>\n')
    file.write('      </rubens>\n')
    file.write('      <stockage>\n')
    file.write('        <option>1</option>\n')
    file.write('        <nbSite>0</nbSite>\n')
    file.write('      </stockage>\n')
    file.write('    </parametresImpressionResultats>\n')
    file.write('    <parametresVariablesCalculees>\n')
    file.write('      <variablesCalculees>false false false false false false false false false false false false false false false</variablesCalculees>\n')
    file.write('    </parametresVariablesCalculees>\n')
    file.write('    <parametresVariablesStockees>\n')
    file.write('      <variablesStockees>true false false false false true true true false false false false false false false false false false false true false false true false false false false false false false false false false false false false false false false false false false</variablesStockees>\n')
    file.write('    </parametresVariablesStockees>\n  </parametresCas>\n</fichierCas>')
    
    file.close()
#    return(0)
    return(Strk_str, 0)

#a, b = crearXCAS(XCAS_new, i, abz_cort, coef_Strk)
