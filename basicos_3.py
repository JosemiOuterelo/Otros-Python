#!/usr/bin/env python 
#-*- coding: utf-8 -*-

i=0
suma=0
lista=[]
cont=int(raw_input("Cuantos numeros va a tener la lista? "))

while(i<cont):
	num=int(raw_input("Introduce numero: "))
	lista.append(num)
	suma+=lista[i]
	i+=1
	
print "Suma Total = ",suma
