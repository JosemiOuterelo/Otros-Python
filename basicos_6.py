#!/usr/bin/env python 
#-*- coding: utf-8 -*-

cont=int(raw_input("Introduce tamaño de la lista : "))
i=0
lista=[]

while(i<cont):
	num=int(raw_input("Introduce numero : "))
	lista.append(num)
	if (lista[i]%2==0):
		print lista[i]," es par"
	else:
		print lista[i]," es impar"
	i+=1
