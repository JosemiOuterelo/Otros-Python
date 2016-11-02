#!/usr/bin/env python 
#-*- coding: utf-8 -*-

lista=[]
cont=int(raw_input("Introduce tamaño de la lista : "))
i=0

while(i<cont):
	num=int(raw_input("Introduce numero : "))
	lista.append(num)
	i+=1
	
print lista

while(cont>0):
	print lista[cont-1]
	cont-=1
