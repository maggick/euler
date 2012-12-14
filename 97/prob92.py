#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

# answer : 8739992577

def puissance2 (n):
    n = (n*2)%10000000000
    return n

def main():
    i = 0
    res = 1
    while (i < 7830457):
        res = puissance2(res)
        i +=1
    res = res*28433 +1
    print res%100000000000

if __name__ == "__main__":
    main()

