#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 31626

def getDivisor(n):
    properDivisor = []
    i = 1
    while (i < n/2 +1):
        if (n % i == 0):
            properDivisor.append(i)
        i += 1
    return properDivisor

def d(n):
    div = getDivisor(n)
    sum = 0
    for elem in div:
        sum += elem
    return sum

def main():
    dic = {}
    n = 1
    res = 0
    while n < 10000:
        dic[d(n)] = n
        if dic.has_key(n) and d(n) == dic[n] and n != d(n):
            res += n + d(n)
        n += 1
    print res

if __name__ == "__main__":
    main()
