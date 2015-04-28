#! /usr/bin/python

import random
from math import *
from re import *
from sympy import *

__test__={}

x=symbols('x')

class Polynomial(object):
	"""
	Class: Polynomial
	
	Represents a polynomial of one variable with random coefficients from -10 to 10.  The class exists sololy to print out polynomials in a readable format.
	"""

	def __init__(self, poly):
		"""
		Invocation: Polynomial(degree)
		Meaning: Take a sympy.expression and turn it into a polynomial object for printing.
		Preconditions: None. 
		Postconditions: Returns a polynomial object.
		"""	
		self.polynomial = poly

	"""
	Field: polynomial
	Type: String
	Meaning: This is the string representation of a polynomial in python format.
	Invariants: None.
	"""
	
	def __repr__(self):
		"""
		>>> from math import *
		>>> from re import *
		>>> from sympy import *
		>>> Polynomial(x**2 + 3*x + 2)
		x^2 + 3x + 2
		"""
		exponent = compile('\*\*')
		carrots = exponent.sub('^', repr(self.polynomial))
		multiplication = compile('\*')
		prettypoly = multiplication.sub('', carrots)
		return prettypoly
			
affirmative=['Y','y','yes', 'YES', 'Yes']  #list of strings accepted as yes
negatory= ['N', 'n', 'no', 'NO', 'No']  #list of strings accepted as no

def makepoly():
	degree=int(round(random.triangular(0.3,3.4,1.7),1))
	polynomial=0
	coefficients= [0]*(degree+1)
	for n in range (degree+1):
		coefficients[n]= random.randint(-10,10)	
		polynomial+= coefficients[n]*x**n
	if degree==0 and coefficients==[0]:
		polynomial=makepoly() #If polynomial is 0 find new polynomial
	return polynomial
	"""
	generates a string representing a random polynomial
	"""
def definefactoring():
	while True:
		factor=raw_input('do you want factoring problems? (Y/N)')
		if factor in affirmative:
			return True
		elif factor in negatory:
			return False
		else:
			print 'Invalid response, reply Y or N'
			
		"""
		Returns true if user indicates factoring problems are wanted and false if they are not wanted.
		"""

def definenumberoffactoring():
	while True:
		nfactor=raw_input('How many factoring problems would you like? (0-5)')
		if nfactor not in ['0','1','2','3','4','5']:
			print 'invalid response'
		else:
			return int(nfactor)
		"""
		Requests the user inputs an integer between 0 and 5 to be the number of factoring problems outputted, returns the integer 
		"""

def definepolynomialadd():
	while True:
		add=raw_input('do you want polynomial addition problems? (Y/N)')
		if add in affirmative:
			return True
		if add in negatory:
			return False
		else:
			print 'Invalid response, reply Y or N'

		"""
		Returns true if problems user indicates addition problems are wanted and false if they are not wanted.
		"""
		
def definenumberofaddition():
	while True:
		nadd=raw_input('How many addition problems would you like? (0-5)')
		if nadd not in ['0','1','2','3','4','5']:
			print 'invalid response'
		else:
			return int(nadd)

		"""
		Requests the user inputs an integer between 0 and 5 to be the number of addition problems outputted, returns the integer.
		"""
		
def definepolynomialmultiplication():
	while True:
		mult=raw_input('do you want polynomial multiplication problems? (Y/N)')
		if mult in affirmative:
			return True
		if mult in negatory:
			return False
		else:
			print 'Invalid response, reply Y or N'

		"""
		Returns true if user indicates multiplication problems are wanted and false if they are not wanted.
		"""

def definenumberofmultiplication():
	while True:
		nmult=raw_input('How many addition problems would you like? (0-5)')
		if nmult not in ['0','1','2','3','4','5']:
			print 'invalid response'
		else:
			return int(nmult)

		"""
		Requests the user inputs an integer between 0 and 5 to be the number of multiplication problems outputted, returns the integer.
		"""

#PROGRAM:
factor=definefactoring()
if factor:
	nfactor=definenumberoffactoring()
	for i in range(nfactor):
		a=makepoly()
		b=makepoly()
		print 'problem:', Polynomial(expand(a*b))
		print 'solution:', '(', Polynomial(a), ')(', Polynomial(b), ')'
		print ' ' #prints a blank line

add=definepolynomialadd()
if add:
	nadd=definenumberofaddition()
	for i in range (nadd):
		a=makepoly()
		b=makepoly()
		print 'problem: (', Polynomial(a), ') + (', Polynomial(b), ')'
		print 'solution:', Polynomial(simplify(a+b))
		print ' ' #prints a blank line
 
mult=definepolynomialmultiplication()
if mult:
	nmult=definenumberofmultiplication()
	for i in range(nmult):
		a=makepoly()
		b=makepoly()
		print 'problem: (', Polynomial(a), ')(', Polynomial(b), ')'
		print 'solution:', Polynomial(expand(a*b))
		print ' ' #prints a blank line


# References
# https://docs.python.org/2/howto/regex.html#regex-howto
#http://docs.sympy.org/latest/index.html
#https://docs.python.org/2/library/random.html
	