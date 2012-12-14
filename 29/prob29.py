#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 9183

def main():
    a = 2
    res = []
    while (a < 101):
        b = 2
        while (b < 101):
            if ((a**b) in res)== False:
                res.append(a**b)
            b += 1
        a += 1
    print len(res)

if __name__ == "__main__":
    main()
