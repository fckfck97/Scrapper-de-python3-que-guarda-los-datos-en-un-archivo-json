#!/usr/bin/python
# -*- coding: utf-8 -*-
#obtener años
from requests import get
from bs4 import BeautifulSoup
import json
from tqdm import tqdm,trange
import time

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	 # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 -Peliculas")
	print ("\t2 -Series")
	print ("\t3 -Animes")
	print ("\t4 -Mostrar Busqueda")
	print ("\t9 - Salir")
 
 

def busqueda(nombre,numero):
	data = {}
	data[nombre] = []
	url = 'https://hackstore.net/'+nombre+'/'
	url2 = 'https://hackstore.net/'+nombre+'/page/'+numero+'/'
	for num in trange(int(numero)):
		if url == 'https://hackstore.net/'+nombre+'/':
			response = get(url)
			res = BeautifulSoup(response.text,"html5lib");
			tags = res.findAll("div",{"class":"movie-back"})
			for tag in tags:
				titulo = tag.h3.getText()
				data[nombre].append({'titulo': titulo})
			tags2 = res.findAll("div", {"class": "movie-back"})
			for tag in tags2:
				ref = tag.a.get("href")
				data[nombre].append({'ref': ref})
			tags3 = res.findAll("div",{"class":"audios"})
			for tag in tags3:
				idioma = tag.getText()
				data[nombre].append({'idioma': idioma})
			with open('data.json', 'w') as file:
				json.dump(data, file, indent=4)

		elif url2 == 'https://hackstore.net/'+nombre+'/page/'+numero+'/':
			response = get(url2)
			res = BeautifulSoup(response.text,"html5lib");
			tags = res.findAll("div",{"class":"movie-back"})
			for tag in tags:
				titulo = tag.h3.getText()
				data[nombre].append({'titulo': titulo})
			tags2 = res.findAll("div", {"class": "movie-back"})
			for tag in tags2:
				ref = tag.a.get("href")
				data[nombre].append({'ref': ref})
			tags3 = res.findAll("div",{"class":"audios"})
			for tag in tags3:
				idioma = tag.getText()
				data[nombre].append({'idioma': idioma})
			with open('data.json', 'w') as file:
				json.dump(data, file, indent=4)

			
		time.sleep(0.001)
	



while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		numero = input("Ingresa el Numero de Paginas a Iterar >> ")
		busqueda("peliculas",numero)
	elif opcionMenu=="2":
		print ("")
		numero = input("Ingresa el Numero de Paginas a Iterar >> ")
		busqueda("series",numero)
	elif opcionMenu=="3":
		print ("")
		numero = input("Ingresa el Numero de Paginas a Iterar >> ")
		busqueda("animes",numero)
	elif opcionMenu=="4":
		print ("")
		nombre = str(input("Ingresa el nombre a buscar: "))
		
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")




	





















