#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)
#answer : 443839

def decomp (n):
    num = []
    while (n != 0):
        num.append(n%10)
        n = n/10
    return num

def sum(num):
    p = 5
    sum = 0
    i = 0
    while (i < len(num)):
        sum = sum + num [i]**p
        i += 1
    return sum

def main():
    n = 2
    res = 0
    while (n < 999999):
        num = decomp (n)
        if (sum(num) == n):
           res += n
        n += 1
    print res

if __name__ == "__main__":
    main()
