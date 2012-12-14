# Resolution project euler 41

__author__ = "matt"
__date__ = "$Oct 06, 2011 9:57:40 PM$"

from math import log10
from math import trunc
# is n prime ?
# Miller-Bach (1985) 

def isPrime (n)
	res = 1

# Le seul nombre premier inferieur a 3 est 2
	if (n < 3):
		if (n != 2):
			res = 0

# Le seul nombre premier pair est 2
	if ((n % 2) == 0):
		res = 0

	if (res != 0):
		# Calcule q tel que n-1=2^r*q
		q = n-1
		r = 0
		while ((q % 2) == 0 and res ==1):
			q /= 2
			r += 1

		a = 2
		amax = trunc(2 * log10(n) * log10(n))
		if (n <= amax):
			amax = n-1

		while (a <= amax and res ==1):
			m = pow(a, q) % n
			if (m != 1):
				if (r != 1):
					ir = 1
					while (m != n-1 and res ==1):
						m = pow(m, 2)
						m = m % n
						ir += 1
						if (r < ir):
							res = 0
				else:
					if (m != n-1):
						res = 0
			a += 1
		res = 1
	print (res)
