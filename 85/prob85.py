#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com>

# answer 2772  : 36*77

def calc (x,y):
    i = 0
    c=0
    while i < x+1:
        j = 0
        while j < y+1:
            c+=i*j
            j+=1
        i+=1
    return c

def main():
    x = 10
    n = 2
    m = 1
    res = 2
    while x < 100:
        y = 10
        while y < 100:
            m = calc (x,y)
            if  m > 1990000 and abs(2000000-m)<abs(2000000-n):
                n = m
                print x, y, n, x*y
                res = x*y
            y+=1
        x+=1
    print res


if __name__ == "__main__":
    main()

