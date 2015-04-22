#! /usr/bin/python

import random
from math import *
import re
from sympy import *

x=symbols('x')

class RandomPolynomial(object):
	"""
	Class: RandomPolynomial
	
	Represents a polynomial of one variable with random coefficients from -10 to 10.
	"""

	def __init__(self, degree=int(round(random.triangular(-0.4,3.4,1.7),1))):
	"""
	Invocation: RandomPolynomial(degree)
	Meaning: Construct a polynomial object of given degree, if no degree is  specified a random degree between zero and 3 is chosen with degrees 1 and 2 most likely.  Coefficients are randomly selected integers between -10 and 10.
	Preconditions: Degree is a non negative integer or not supplied.
	Postconditions: A polynomial of given degree is returned with randomly selected coefficients. If no degree is  specified a random degree between zero and 3 is chosen with degrees 1 and 2 most likely.
	"""	
		if type(degree) != int:
			raise ValueError('Degree must be an integer but instead was' + repr(type(degree)))
		coefficients= [0]*(degree+1)
		polynomial=0	
		for n in range (degree+1):
			coefficients[n]= random.randint(-10,10)	
			polynomial+= coefficients[n]*x**n
		self.polynomial = polynomial

	"""
	Field: polynomial
	Type:
	Meaning:
	Invariants:
	"""
	
	#def __repr__(self):
	#exponent = re.compile('**')
	#carrots = re.compile(exponent.sub('^', str(self.polynomial)))
	#multiplication = re.compile('*')
	#prettypoly = multiplication.sub(", str(carrots))
	#return prettypoly
	
	
	
		
def definefactoring():
	while True:
		factor=raw_input('do you want factoring problems? (Y/N)')
		if factor=='Y':
			return True
		elif factor=='N':
			return False
		else:
			print 'Invalid response, reply Y or N'
			
	"""
	Returns true if problems user indicates factoring problems are wanted and false if they are not wanted.
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
		if add =='Y':
			return True
		if add=='N':
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
    Requests the user inputs an integer between 0 and 5 to be the number of addition problems outputted, returns the integer 
    """

#def makeadditionproblem():
		
def definepolynomialmultiplication():
	while True:
		mult=raw_input('do you want polynomial multiplication problems? (Y/N)')
		if mult=='Y':
			return True
		if mult=='N':
			return False
		else:
			print 'Invalid response, reply Y or N'

	"""
	Returns true if problems user indicates multiplication problems are wanted and false if they are not wanted.
	"""

def definenumberofmultiplication():
	while True:
		nmult=raw_input('How many addition problems would you like? (0-5)')
		if nmult not in ['0','1','2','3','4','5']:
			print 'invalid response'
		else:
			return int(nadd)

    """
    Requests the user inputs an integer between 0 and 5 to be the number of multiplication problems outputted, returns the integer 
    """


factor=definefactoring()
if factor:
	nfactor=definenumberoffactoring()
	for i in range (nfactor):
		a=RandomPolynomial()
		b=RandomPolynomial()
	print 'problem:', expand(a.polynomial*b.polynomial)
	print 'solution:', '(', a.polynomial, ')(', b.polynomial, ')'
	print ' ' #prints a blank line​

add=definepolynomialadd()
if add:
	nadd=definenumberofaddition()
	for i in range (nadd):
		a=RandomPolynomial()
		b=RandomPolynomial()
	print 'problem:', a.polynomial, '+', b.polynomial 
	print 'solution:', simplify(a.polynomial+b.polynomial)
	print ' ' #prints a blank line
 
mult=definepolynomialmultiplication()
if mult:
	nmult=definenumberofmultiplication()
	for i in range(nmult):
		a=RandomPolynomial()
		b=RandomPolynomial()
	print 'problem: (', a.polynomial, ')(', b.polynomial, ')'
	print 'solution:', expand(a.polynomial*b.polynomial)
	print ' ' #prints a blank line


# References
# https://docs.python.org/2/howto/regex.html#regex-howto
#http://docs.sympy.org/latest/index.html
#https://docs.python.org/2/library/random.html
	