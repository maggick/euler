#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 872187


def toBinary (n):
    res = []
    while n > 1:
        if (n%2):
            res.append(1)
        else :
            res.append(0)
        n = n/2
    if n == 1:
        res.append(1)
    else:
        res.append(0)
    return res

def toList (n):
    res = []
    while (n >= 1):
        res.append(n%10)
        n = n /10
    return res

def isPalindrom (list):
    i = 0
    cont = True
    if len(list)< 2:
        return cont
    else:
        while i < len(list)/2+1 and cont:
            if list[i] != list[len(list) -1-i]:
                cont = False
            i +=1
        return cont

def main():
    n = 1
    sum = 0
    while n <= 1000000:
        if isPalindrom(toList (n)) and isPalindrom(toBinary(n)):
            sum += n
        n +=1
    print sum

if __name__ == "__main__":
    main()

