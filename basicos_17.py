#!/usr/bin/env python 
#-*- coding: utf-8 -*-

lista=[]
mayor=0

n=int(raw_input("Introduuce cantidad de numeros : "))

while(n>0):	
	x=int(raw_input("Introduuce numero : "))
	lista.append(x)
	n-=1

for ele in lista:
	if (ele>mayor):
		mayor=ele
	
print "El numero mayor es ",mayor
