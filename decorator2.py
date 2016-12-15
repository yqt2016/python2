#!/usr/bin/env python
#FileName:decorator2.py
import functools
def log(text):
	if callable(text):
		@functools.wraps(text)
		def wrapper(*args, **kw):
			print 'begin call: ' + text.__name__
			text(*args, **kw)
			print 'end call: ' + text.__name__
		return wrapper
	else:
		def decorator(func): 
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print 'begin call: ' + text
				func(*args, **kw)
				print 'end call: ' + text
			return wrapper
		return decorator
@log
def now():
	print '2016-12-15'
now()
@log('call')
def now2():
	print '2016-12-15'
now2()	
