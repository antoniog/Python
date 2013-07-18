#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
#
#       sin título.py
#
#       Copyright 2011 el usuario necrolord <necrolord@newton>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#

import os
import win32api
import sys
import re
import datetime
#-------archivo ini
homedir = os.path.expanduser("~")
#conffile = homedir+"\menu_navegadores.ini"
conffile = "menu_navegadores.ini"


#-------menú principal
def menu():
    os.system('cls')
    if os.path.exists(uniex+'ttgo.bif') == 1:
        menuNAVTOM()
    elif os.path.exists(uniex+'ttnavigator.bif')==1:
        menuPDASOFT()
    else:
        print ("MENÚ DE SOFTWARE DE NAVEGADOR BY NECRO")
        print ("========================================")
        print ("")
        print ("|---------------|")
        print ("|               |")
        print ("|  1: GPS       |")
        print ("|               |")
        print ("|  2: PDA       |")
        print ("|               |")
        print ("|               |")
        print ("|  0: Salir     |")
        print ("|               |")
        print ("|---------------|")
        op=int(input("Elige una opción: "))
        if (op == 1):
            menuNAVSOFT()
        elif (op == 2):
            menuPDASOFT()
        elif (op == 0):
            salida()
    #-------reintentos en caso de fallo
        retries = 4
        while op < 1 or op > 2:
            print ("")
            print ("¡¡Elige una opción correcta!!")
            print ("")
            retries = retries - 1
            if retries < 0:
                print("Aprende a leer!")
                salida()
            op=int(input("Elige una opción: "))


#-------menú gps navegador -> software
def menuNAVSOFT():
    os.system('cls')
    print ("<- Menú GPS en", uniex)
    print ("")
    print ("|---------------|")
    print ("|               |")
    print ("|  1: TomTom    |")
    print ("|               |")
    print ("|  2: Sygic     |")
    print ("|               |")
    print ("|  3: Otros     |")
    print ("|               |")
    print ("|               |")
    print ("|  0: Volver    |")
    print ("|               |")
    print ("|---------------|")
    ans=int(input("Elige una opción: "))

    if (ans==1): menuNAVTOM()
    elif (ans==2): menuNAVSYG()
    elif (ans==3): menuNAVOTR()
    elif (ans==0): menu()

    retries=2
    while ans<1 or ans>3 and ans!=0:
        print ("")
        print ("¡¡Elige una opción correcta!!")
        print ("")
        retries=retries-1
        if retries<0:
            print("Aprende a leer!")
            salida()
        ans=int(input("Elige una opción: "))

#-------menú gps>software>tomtom> acciones
def menuNAVTOM():
    os.system('cls')
    print ("<- Menú TOMTOM en", uniex)
    print ("")
    print (".---------------------------------------------------------------------.")
    print ("|                                                                     |")
    print ("|  1: Actualizar/Instalar Nav + Iberia + pdi                          |")
    print ("|                                                                     |")
    print ("|  2: Actualizar/Instalar Nav + Iberia no-carriles + pdi              |")
    print ("|                                                                     |")
    print ("|  3: Actualizar/Instalar Nav + South Europe + East (2GB) + pdi       |")
    print ("|                                                                     |")
    print ("|  4: Actualizar/Instalar Nav + South Europe 1GB no-carriles + pdi    |")
    print ("|                                                                     |")
    print ("|  5: Actualizar/Instalar Nav + Europe TRUCKS + pdi                   |")
    print ("|                                                                     |")
    print ("|  6: Actualizar/Instalar Nav + Europe +2GB + pdi                     |")
    print ("|                                                                     |")
    print ("|                                                                     |")
    print ("|  0: Volver                                                          |")
    print ("|                                                                     |")
    print (".---------------------------------------------------------------------.")
    ans=int(input("Elige una opción: "))
#-------función de actualización navegador TomTom
    def actualiza(mapa):
        ttgobifurl = (uniex+'ttgo.bif')
        if os.path.exists(ttgobifurl)==1:
            with open(ttgobifurl, mode='r') as ttgofileopn:
                fullcontent = ttgofileopn.read()
                idttgobif = fullcontent.find("DeviceUniqueID=")
                ttgofileopn.seek(idttgobif+21)
                deviceID = (ttgofileopn.read(11)).replace(' ','')
                print ("DeviceID [",deviceID,"] almacenado en memoria...OK")
                print ("#")
                print ("#")
                print ("#")

        os.system ("cls")
        def bakfilesclean():
            if os.path.exists(ttgobifurl)==1:
                os.system ("copy %s %s" % (uniex+'ttgo.bif', homedir))
                print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " COPIADO ARCHIVO 'ttgo.bif'...OK")
                for r,d,f in os.walk(uniex):
                    for files in f:
                        if files.endswith("mapsettings.cfg"):
                             fullpath = (os.path.join(r,files))
                             onlypath = fullpath[:-15]
                             os.system ("copy %s %s" % (uniex+'mapsettings.cfg', homedir))
                             print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " COPIADO ARCHIVO 'mapsettings.cfg'...OK"
                os.system ("format /Q /X /V:TomTom %s" % ((uniex).rstrip('\\')))
                print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " BORRADO VOLUMEN COMPLETO...OK")
                os.system ("move %s %s" % (homedir+'"\\"ttgo.bif', uniex))
                print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " RESTAURADO 'ttgo.bif'...OK")
                os.system ("move %s %s" % (homedir+'"\\"mapsettings.cfg', uniex))
                print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " RESTAURADO 'mapsettings.cfg'...OK")
            else:
                print ("ttgo.bif NO PRESENTE")
                os.system ("format /Q /X /V:TomTom %s" % ((uniex).rstrip('\\')))
                print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " BORRADO VOLUMEN COMPLETO...OK")

        bakfilesclean()

        if mapa==1:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Iberia', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA IBERIA COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Iberia'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Iberia'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        elif mapa==2:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Iberia_basico', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA IBERIA NO-CARR COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Iberia\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Iberia\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        elif mapa==3:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA SOUTH EUROPE COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'South_Europe_2GB\\South_Europe', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA SOUTH EUROPE COPIADO CON ÉXITO...OK")
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA EASTERN EUROPE COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Eastern_Europe_basico\\Eastern_Europe', uniex+'Eastern_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA EASTERN EUROPE COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        elif mapa==4:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA SOUTH EUROPE 1GB COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'South_Europe_1GB\\South_Europe', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA SOUTH EUROPE 1GB COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'South_Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        elif mapa==5:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'v9\\_Camion\\nav_truck\\', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE TRUCK ESPECIAL COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Europe_TRUCK\\Europe_TRUCK\\', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA EUROPE TRUCK COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Europe_TRUCK\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'Europe_TRUCK\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Europe_TRUCK\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        elif mapa==6:
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
            os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Europe_2GB\\Europe\\', uniex))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " MAPA EUROPE >2GB COPIADO CON ÉXITO...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
            os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Europe\\'))
            print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")

        os.system("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares', uniex+'sounds\\'))
        print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " SONIDOS DE PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
        print ("#")
        print ("#")
        os.system("xcopy %s %s /E /Q /Y" % (voces+'voices', uniex+'voices\\'))
        print ("[",datetime.datetime.now().strftime("%H:%M:%S"),"].", " VOCES PREGRABADAS MULTI-LENGUAJE COPIADAS CON ÉXITO...OK")
        os.system("cd D:\appz\02_GPS\00_TOMTOM\01_MAPAS\02_Activadores\Activador Mapas V7-V8")
        os.system("d:")
        os.system("Activador Mapas V7-V8.cmd")
        print ("#")
        print ("#")
        print ("#############################################")
        print ("#                                           #")
        print ("##       TOMTOM INSTALADO CON ÉXITO        ##")
        print ("#                                           #")
        print ("#############################################")
        input("PULSA ENTER PARA SALIR...")
        salida()

    if (ans==1): actualiza(1)
    elif (ans==2): actualiza(2)
    elif (ans==3): actualiza(3)
    elif (ans==4): actualiza(4)
    elif (ans==5): actualiza(5)
    elif (ans==6): actualiza(6)
    elif (ans==0): menuNAVSOFT()
    elif (ans!=1,2,3,4,5,6,0):
        print ("Haber elegido una opción correcta")
        salida()
#-------menú gps>software> sygic
def menuNAVSYG():
    os.system('cls')
    print ("<- Has elegido Sygic")
    print ("====================")
    print ("")
    print ("Elige acción:")
    print ("=============")
    print ("")
    print ("        1.2.1 Instalar Sygic Iberia + pdi")
    print ("        1.2.2 Instalar Sygic Full Europe > 2GB + pdi")
    print ("")
    print ("        1.2.0 Volver")
    print ("")
    ans=input("Elige una opción: ")
    print ("")
    print ("    1.Android")
    print ("    2.Symbian")
    print ("    3.Windows Mobile")
    os=input("Elige el Sistema Operativo: ")
    if (ans=='1' & os=='1'): instala(syib,pdis,an)
    elif (ans=='1' & os=='2'): instala(syib,pdis,sy)
    elif (ans=='1' & os=='3'): instala(syib,pdis,wm)
    elif (ans=='2' & os=='1'): instala(syeu,pdis,an)
    elif (ans=='2' & os=='2'): instala(syeu,pdis,sy)
    elif (ans=='2' & os=='3'): instala(syeu,pdis,wm)
    elif (ans!=1,2,0 | ans!=1,2,3): print ("elige una opción correcta")
#-------
def salida():
    sys.exit(0)
#---------------------------- FIN DE FUNCIONES

with open(conffile, mode='r', encoding='utf-8') as conffileopn:
    print ("Archivo de configuración leído OK.")
    print ("")
    infile=conffileopn.readlines()
    tomdir=((infile[0])[7:]).rstrip('\n')
    navcores=(tomdir+(infile[1])[9:]).rstrip('\n')
    mapas=(tomdir+(infile[2])[6:]).rstrip('\n')
    pdis=(tomdir+(infile[3])[5:]).rstrip('\n')
    voces=(tomdir+(infile[4])[6:]).rstrip('\n')

drives = win32api.GetLogicalDriveStrings()
print (".---------------------------------------------------------------------.")
print ("|  UNIDADES DETECTADAS                                                |")
print (".---------------------------------------------------------------------.")
print (drives)
print ("")
uniexinput=input("Introduce la unidad de trabajo: ")
uniex=uniexinput+":\\"
if re.match("([A-Za-z])", uniex):
    print ("Unidad seleccionada", uniex)
else:
    print ("¡¡Introduce una unidad de trabajo válida!!")
    print ("")
    salida()

if os.path.exists(uniex+'ttgo.bif')==1:
    ttgobifurl = (uniex+'ttgo.bif')
    with open(ttgobifurl, mode='r') as ttgofileopn:
        fullcontent = ttgofileopn.read()
        refursearch = fullcontent.find("BootLoaderVersion=10")
        print ("COMPROBANDO TOMTOM REFURBISHED...")
        print ("#")
        print ("#")
        if refursearch > 0:
            print ("#")
            print ("#")
            print ("#############################################")
            print ("#                                           #")
            print ("##       ¡¡¡¡TOMTOM REFURBISHED!!!!        ##")
            print ("#                  WARNING                  #")
            print ("#                                           #")
            print ("#############################################")
            input("PULSA ENTER PARA SALIR...")
            salida()
        elif refursearch < 0:
            menu()
else:
    menu()
