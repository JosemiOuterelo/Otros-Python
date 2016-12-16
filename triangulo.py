#!/usr/bin/env python 
#-*- coding: utf-8 -*-

n = int(raw_input("Mete a saco ahi un numero:"))

cont=1

for x in range(0,n+1):
	f=x
	while f>0:
		print cont,
		cont+=1
		f-=1
	print " "
	
