#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def fun(num):
	cont=0
	while(num>0):
		num=num/10
		cont+=1
	return cont
