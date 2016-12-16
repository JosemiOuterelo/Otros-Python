#!/usr/bin/env python 
#-*- coding: utf-8 -*-

a=50;
colecc=[]
while a>0:
	n=int(raw_input("Introduce numero : "));
	colecc.append(n)
	a-=1

mayor=0
menor=100000
contmy=0
contmn=0

for ele in colecc:
	if ele > mayor:
		mayor=ele
	if ele < menor:
		menor=ele

for ele in colecc:
	if ele==mayor:
		contmy+=1
	if ele==menor:
		contmn+=1

print mayor," es el numero mayor y ha aparecido ",contmy," veces"
print menor," es el numero menor y ha aparecido ",contmn," veces"
