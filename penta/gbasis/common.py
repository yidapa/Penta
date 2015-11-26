#fwf


def fac(n):
	'''
	the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers
	less than or equal to n.
	'''
	if n<=0:
		return 1
	else:
		return n * fac(n-1)

def fac2(n):
	'''The double factorial, symbolized by two exclamation marks (!!), is a quantity defined for all
	integer s greater than or equal to -1. For an even integer n , the double factorial is the prod-
	uct of all even integers less than or equal to n but greater than or equal to 2. For an odd int-
	eger p , the double factorial is the product of all odd integers less than or equal to p and gr-
	eater than or equal to 1. The double factorial values of 0 and -1 are defined as equal to 1. Do-
	uble factorial values for integers less than -1 are not defined.
	'''
	if n<=0:
		return 1
	else:
		return n * fac2(n-2)

def binom(n, m):
	numer = 1
	denom = 1
	while (n > m):
		numer *= n
		denom *= n-m
		n = n-1
	return numer/denom

##############################################
# Auxiliary functions for Gaussian integrals #
##############################################

def gb_overlap_int1d(n0, n1, pa, pb, gamma_inv):
	kmax = (n0+n1)/2
	result = 0.0
	for k in range(kmax):
		result += fac2(2*k-1)*gpt_coeff(2*k, n0, n1, pa, pb)*
	
