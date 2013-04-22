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

import os, win32api, sys, re, datetime
#-------archivo ini
homedir = os.path.expanduser("~")
#conffile = homedir+"\menu_navegadores.ini"
conffile = "menu_navegadores.ini"
# tiempo
now = datetime.datetime.now()
homise = now.strftime("%H:%M:%S")

#-------menú principal
def menu():
	os.system('cls')
	if os.path.exists(uniex+'ttgo.bif')==1:
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
		if (op==1):
			menuNAVSOFT()
		elif (op==2):
			menuPDASOFT()
		elif (op==0):
			salida()
	#-------reintentos en caso de fallo
		retries=4
		while op<1 or op>2:
			print ("")
			print ("¡¡Elige una opción correcta!!")
			print ("")
			retries=retries-1
			if retries<0:
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
	print ("|---------------------------------------------------------------------|")
	print ("|                                                                     |")
	print ("|  1: Actualizar/Instalar Nav + Iberia + pdi                          |")
	print ("|                                                                     |")
	print ("|  2: Actualizar/Instalar Nav + Iberia no-carriles + pdi              |")
	print ("|                                                                     |")
	print ("|  3: Actualizar/Instalar Nav + South Europe + East (2GB) + pdi       |")
	print ("|                                                                     |")
	print ("|  4: Actualizar/Instalar Nav + South Europe no-carriles < 2GB + pdi  |")
	print ("|                                                                     |")
	print ("|  5: Actualizar/Instalar Nav + Europe TRUCKS + pdi                   |")
	print ("|                                                                     |")
	print ("|                                                                     |")
	print ("|  0: Volver                                                          |")
	print ("|                                                                     |")
	print ("|---------------------------------------------------------------------|")
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
		def protectttgobif():
			if os.path.exists(ttgobifurl)==1:
				os.system ("attrib +r %s" % (ttgobifurl))
				print (homise, " PROTEGIDO ARCHIVO 'ttgo.bif'...OK")
				print ("#")
				print ("#")
				os.system ("del /S /Q /A:-R %s" % ((uniex).rstrip('\\')))
				#os.system ("del /S /Q /A:-R %s" % ((uniex)))
				print (homise, " BORRADO VOLUMEN COMPLETO...OK")
				print ("#")
				print ("#")
				os.system ("attrib -r %s" % (ttgobifurl))
				print (homise, " RESTAURADO 'ttgo.bif'...OK")
				print ("#")
				print ("#")
			else:
				print ("ttgo.bif NO PRESENTE")
				os.system ("del /S /Q %s" % ((uniex).rstrip('\\')))
				print (homise, " BORRADO VOLUMEN COMPLETO...OK")
				print ("#")
				print ("#")

		if mapa==1:
			protectttgobif()
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
			print ("NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Iberia', uniex))
			print (homise, " MAPA IBERIA COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Iberia'))
			print (homise, " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Iberia'))
			print (homise, " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")
			print ("#")
			print ("#")
			
		elif mapa==2:
			protectttgobif()
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Iberia_basico', uniex))
			print (homise, " MAPA IBERIA NO-CARR COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Iberia\\'))
			print (homise, " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Iberia\\'))
			print (homise, " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")
			print ("#")
			print ("#")
			
		elif mapa==3:
			protectttgobif()
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			print (homise, " MAPA SOUTH EUROPE COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'South_Europe_2GB\\South_Europe', uniex+'South_Europe\\'))
			print (homise, " MAPA SOUTH EUROPE COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			print (homise, " MAPA EASTERN EUROPE COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Eastern_Europe_basico\\Eastern_Europe', uniex+'Eastern_Europe\\'))
			print (homise, " MAPA EASTERN EUROPE COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'South_Europe\\'))
			print (homise, " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'South_Europe\\'))
			print (homise, " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
			print (homise, " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'South_Europe\\'))
			print (homise, " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")
			print ("#")
			print ("#")

		elif mapa==4:
			protectttgobif()
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (navcores+'_RECOMENDADO_TUNEADO', uniex))
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			print (homise, " MAPA SOUTH EUROPE 1GB COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'South_Europe_1GB\\South_Europe', uniex+'South_Europe\\'))
			print (homise, " MAPA SOUTH EUROPE 1GB COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			print (homise, " MAPA EASTERN EUROPE COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Eastern_Europe_basico\\Eastern_Europe', uniex+'Eastern_Europe\\'))
			print (homise, " MAPA EASTERN EUROPE COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'South_Europe\\'))
			print (homise, " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'South_Europe\\'))
			print (homise, " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
			print (homise, " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'South_Europe\\'))
			print (homise, " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")
			print ("#")
			print ("#")
			
		elif mapa==5:
			protectttgobif()
			print (homise, " NAVCORE RECOMENDADO ACTUAL COPIA INICIADA...")
			os.system ("xcopy %s %s /E /Q /Y" % (navcores+'v8\\GPS_RECEPTOR\\_camion\\8.391', uniex))
			print (homise, " NAVCORE TRUCK ESPECIAL COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (mapas+'Europe_TRUCK\\Europe_TRUCK\\', uniex))
			print (homise, " MAPA EUROPE TRUCK COPIADO CON ÉXITO...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares', uniex+'Europe_TRUCK\\'))
			print (homise, " PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'radares_euro', uniex+'Europe_TRUCK\\'))
			print (homise, " PUNTOS DE INTERÉS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares_euro', uniex+'sounds\\Radar\\'))
			print (homise, " SONIDOS PDIS EUROPA COPIADOS CON ÉXITO EN SOUTH EUROPE...OK")
			print ("#")
			print ("#")
			os.system ("xcopy %s %s /Q /Y" % (mapas+'00_MAPSETTINGS\\mapsettings.cfg', uniex+'Europe_TRUCK\\'))
			print (homise, " CONFIGURADA ASOCIACIÓN PDI'S BÁSICOS + VOCES...OK")
			print ("#")
			print ("#")

		os.system("xcopy %s %s /E /Q /Y" % (pdis+'sounds_radares', uniex+'sounds\\'))
		print (homise, " SONIDOS DE PUNTOS DE INTERÉS BÁSICOS COPIADOS CON ÉXITO...OK")
		print ("#")
		print ("#")
		os.system("xcopy %s %s /E /Q /Y" % (voces+'voices', uniex+'voices\\'))
		print (homise, " VOCES PREGRABADAS MULTI-LENGUAJE COPIADAS CON ÉXITO...OK")
		print ("#")
		print ("#")
		os.system("cls")
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
	elif (ans==0): menuNAVSOFT()
	elif (ans!=1,2,3,4,5,0):
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
	print ("		1.2.1 Instalar Sygic Iberia + pdi")
	print ("		1.2.2 Instalar Sygic Full Europe > 2GB + pdi")
	print ("")
	print ("		1.2.0 Volver")
	print ("")
	ans=input("Elige una opción: ")
	print ("")
	print ("	1.Android")
	print ("	2.Symbian")
	print ("	3.Windows Mobile")
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
print ("|---------------------------------------------------------------------|")
print ("|  UNIDADES DETECTADAS                                                |")
print ("|---------------------------------------------------------------------|")
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
			print ("TOMTOM REFURBISHED!! STOP")
			salida()
		elif refursearch < 0:
			menu()
else:
	menu()
