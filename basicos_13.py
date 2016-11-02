#!/usr/bin/env python 
#-*- coding: utf-8 -*-

x=int(raw_input("Introduce primer numero : "))
y=int(raw_input("Introduce segundo numero : "))

if (x>y):
	print x," es mayor que ",y
elif (y>x):
	print y," es mayor que ",x
elif (x==y):
	print "Son iguales"
