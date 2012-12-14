#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 40730


def fact(n):
    if n == 0:
        return 1
    else:
        res = 1
        while n > 1:
            res *= n
            n -= 1
        return res

def decomp (n):
    num = []
    while (n != 0):
        num.append(n%10)
        n = n/10
    return num

def sumFact (num):
    sum = 0
    for n in num:
        sum += fact(n)
    return sum

def op (n):
    return sumFact(decomp(n))

def main():
    n = 3
    res = 0
    while (n < 1000000):  # we stop at 999,999,999 cause op (n) < n
        if (op(n) == n):
            res += n
        n +=1
    print res

def test ():
    print op(145)

if __name__ == "__main__":
    main()
