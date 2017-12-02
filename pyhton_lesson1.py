#!/usr/bin/env python

# -*- coding:utf-8 -*-
"""
to learn about the charactor of python language
"""

import numpy as np
import math


def print_outer():

	name=input('please input your name:')
	print("hi",name)

def insert_list(listgiven,index,item):
	listgiven.insert(index,item)
	print(listgiven)

def example_input():
	age=input("age:")
	if age<30:
		print('we are young!')
	else:
		print('we need to strive!')

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

def quadratic(a,b,c):
	m=(b+math.sqrt(pow(b,2)-4*a*c))/(-2*a)
	n=(b-math.sqrt(pow(b,2)-4*a*c))/(-2*a)
	return m,n

def return_func(*args):
	def sum():
		ax=0
		for n in args:
			ax+=n
		return ax
	return sum
	
def num_counter():
	num=0
	def f():
		nonlocal num
		num+=1
		#print(num)
		return num
	return f



if __name__=='__main__':
	#print_outer()
	a=['I','love','a','person','named']
	#insert_list(a,5,'tla001')
	#example_input()    #not ok!
	#my_value=my_abs(20)
	#m,n=quadratic(1,3,-4)
	#print('m=%d,n=%d'%(m,n))
	# out=return_func(1,3,5,6)
	# print(out)
	# print(out())
	b=num_counter()
	print(b())
	c=num_counter()
	print('fgggggg')
	d=b()+c()
	print(d)



