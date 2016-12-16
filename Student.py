#!/usr/bin/env python
#FileName:Student.py
#config:utf-8
class Student(object):

	def __init__(self,name,score):

		self.name=name

		self.score=score

	def print_score(self):

		print '%s:%s'%(self.name,self.score)

	def get_grade(self):

		if self.score>=90:

			return 'A'

		elif self.score>=60:

			return 'B'

		else:

			return 'C'


yww = Student('yuweiwei',90)
hmm = Student('hanmeimei',58)
print yww.get_grade()
print hmm.get_grade()

