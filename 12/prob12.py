#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 76576500


import operator

def triangle (n):
    tri = 0
    while (n > 0):
        tri += n
        n -= 1
    return tri

# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)


def main ():
    n = 1
    cont = True
    while (cont):
        if NumberOfDivisors(triangle(n)) > 500:
            print triangle(n)
            cont = False
        else : 
            n+=1

if __name__ == "__main__":
    main()
