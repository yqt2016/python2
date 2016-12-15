#!/usr/bin/env python
#FileName:decorator.py
import functools
def now():
	print '2016-12-15'
print(now.__name__)

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'begin call'
		func(*args,**kw)
		print 'end call'
	return wrapper
now=log(now)
now()
print(now.__name__)

def now2():
	print '2016-12-15 15:00'

def log2(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print 'begin %s'%text
			func(*args,**kw)
			print 'end %s'%text
		return wrapper
	return decorator
now2=log2('call')(now2)
now2()
print(now2.__name__)
		
