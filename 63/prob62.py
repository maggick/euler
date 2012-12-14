#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

def numLength (n):
    length = 0
    while (n > 0.1):
        length +=1
        n /=10
    return length

def main ():
    a = 16807
    res = 0
    while a < 1000000000:
        b = 2
        plop = b**numLength(a)
        while (plop <= a):
            if (a == plop):
                res +=1
            b +=1
            plop = b**numLength(a)
        a +=1
    print res

if __name__ == "__main__":
    main()

