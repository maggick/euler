#!/usr/bin/env python3

'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

It turns out that F541, which contains 113 digits, is the first
Fibonacci number for which the last nine digits are 1-9 pandigital
(contain all the digits 1 to 9, but not necessarily in order). And
F2749, which contains 575 digits, is the first Fibonacci number for
which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine
digits AND the last nine digits are 1-9 pandigital, find k.
'''


def isPandigital(n):
    i = 1
    while i < 10:
        if str(i) not in n:
            return False
        i += 1
    return True


def main():
    i = 3
    a = 1
    b = 1
    cont = True
    while cont:
        tmp = a
        a = a + b
        b = tmp
        i += 1
        if isPandigital(str(a)[-9:]) and isPandigital(str(a)[:9]):
            cont = False
    print (i-1)

if __name__ == '__main__':
    main()
