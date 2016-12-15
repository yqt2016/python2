#!/usr/bin/env python
#FileName:lambda.py
def fun1(x,y):
	return lambda :x*x+y*y
f=fun1(1,2)
print f
print f()
def fun2(x,y):
	return lambda x,y:x*x+y*y
f=fun2(1,2)
print f
print f(1,2)
