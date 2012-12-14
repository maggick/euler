#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 669171001

def main():
    i = 0
    res = 1
    n= 1
    c = 0
    while (i/4 < 500):
        n += ((i/4)+1)*2
        res +=n
        i += 1
    print res

if __name__ == "__main__":
    main()
