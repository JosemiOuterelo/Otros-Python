#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def money(dinero):
	cont500=0
	cont200=0
	cont100=0
	cont50=0
	cont20=0
	cont10=0
	cont5=0
	cont2=0
	cont1=0
	cont50c=0
	cont20c=0
	cont10c=0
	cont5c=0
	cont2c=0
	cont1c=0
	while(dinero-500>=0):
		dinero=dinero-500
		cont500+=1
	if(cont500>0):
		print cont500,"billetes de 500" 
	while(dinero-200>=0):
		dinero=dinero-200
		cont200+=1
	if(cont200>0):
		print cont200,"billetes de 200"
	while(dinero-100>=0):
		dinero=dinero-100
		cont100+=1
	if(cont100>0):
		print cont100,"billetes de 100"
	while(dinero-50>=0):
		dinero=dinero-50
		cont50+=1
	if(cont50>0):
		print cont50,"billetes de 50"
	while(dinero-20>=0):
		dinero=dinero-20
		cont20+=1
	if(cont20>0):
		print cont20,"billetes de 20"
	while(dinero-10>=0):
		dinero=dinero-10
		cont10+=1
	if(cont10>0):
		print cont10,"billetes de 10"
	while(dinero-5>=0):
		dinero=dinero-5
		cont5+=1
	if(cont5>0):
		print cont5,"billetes de 5"
	while(dinero-2>=0):
		dinero=dinero-2
		cont2+=1
	if(cont2>0):
		print cont2,"monedas de 2"
	while(dinero-1>=0):
		dinero=dinero-1
		cont1+=1
	if(cont1>0):
		print cont1,"monedas de 1"
	while(dinero-0.50>=0):
		dinero=dinero-0.50
		cont50c+=1
	if(cont50c>0):
		print cont50c,"monedas de 50 cent"
	while(dinero-0.20>=0):
		dinero=dinero-0.20
		cont20c+=1
	if(cont20c>0):
		print cont20c,"monedas de 20 cent"
	while(dinero-0.10>=0):
		dinero=dinero-0.10
		cont10c+=1
	if(cont10c>0):
		print cont10c,"monedas de 10 cent"
	while(dinero-0.05>=0):
		dinero=dinero-0.05
		cont5c+=1
	if(cont5c>0):
		print cont5c,"monedas de 5 cent"
	while(dinero-0.02>=0):
		dinero=dinero-0.02
		cont2c+=1
	if(cont2c>0):
		print cont2c,"monedas de 2 cent"
	while(dinero-0.01>=0):
		dinero=dinero-0.01
		cont1c+=1
	if(cont1c>0):
		print cont1c,"monedas de 1 cent"
		
		
		
