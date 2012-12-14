#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 972


def sum (n):
    res = 0
    while (n > 0.1):
        res += n%10
        n /= 10
    return res


def main():
    maxi = 0
    a = 0
    while (a < 100):
        b = 0
        while (b < 100):
            ret = sum (a**b)
            if (ret>maxi):
                maxi = ret
            b+=1
        a+=1
    print maxi

if __name__ == "__main__":
    main()

