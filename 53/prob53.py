#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 4075


def fact(n):
    if (n == 0 or n == 1):
        return 1
    else :
        i = 1
        res = 1
        while (i <= n):
            res *= i
            i+=1
        return res

def combination (n, r):
    return fact(n)/(fact(r)*fact(n-r))

def main ():
    n = 0
    res = 0
    while (n < 101):
        r = 0
        while (r < 101):
            if combination(n,r)>1000000 :
                res +=1
            r +=1
        n +=1
    print res

if __name__ == "__main__":
    main()

