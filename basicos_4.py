#!/usr/bin/env python 
#-*- coding: utf-8 -*-

lista=[]
i=0
cont=0

cont=int(raw_input("Introduce tamaño de la lista : "))

while(i<cont):
	num=int(raw_input("Introduce numero : "))
	lista.append(num)
	i+=1

opcion=str(raw_input("Introduce opcion deseada : "))

if (opcion=="sumar"):
	suma=0
	for ele in lista:
		suma+=ele
	print "Suma = ",suma
elif(opcion=="restar"):
	resta=0
	for ele in lista:
		resta-=ele
	print "Resta = ",resta
