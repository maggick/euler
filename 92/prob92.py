import math

def sumsquare (n):
	if n == 10:
		return 1
	if n < 10:
		ret=n**2
	else :
		ret = 0
		while n> 10:
			ret+= (n%10)**2
			n /=10
		ret += (n%10)**2
	return ret

def chain (n):
	while True :
		if n == 1 or n == 89:
			return n
		else :
			n = sumsquare(n)

if __name__ == '__main__':
	#print (sumsquare(44))
	#print (sumsquare(32))
	#print (sumsquare(13))
	#print (sumsquare(10))
	print (chain(44))
	print (chain(85))
	i = 2
	res = 0
	while i < 10000000:
		print i
		if chain(i) == 89:
			res+=1
		i+=1
	print res

