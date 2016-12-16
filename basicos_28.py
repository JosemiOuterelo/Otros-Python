#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def divisor(n1,n2):
	d=False
	if n1%n2==0:
		d=True
	return d
	
	

num=int(raw_input("Introduce numero : "));
div=False

for ele in range(num+1):
	ele+=1
	div=divisor(num,ele)
	if div==True:
		print ele," es divisor."
	
