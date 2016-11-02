#!/usr/bin/env python 
#-*- coding: utf-8 -*-

n=int(raw_input("Mostrar tabla de multiplicar de los ..."))

while(n>0):
	for ele in range(11):
		print n," x ",ele," = ",n*ele
	n-=1
