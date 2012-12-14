#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com)

#answer : 142857

def decom (n):
    liste = []
    while (n > 0.1):
        liste.append(n%10)
        n /= 10
    return liste

def comp (n, m):
    num1 = decom (n)
    num2 = decom (m)
    if (len(num1) == len(num2)) :
        num1.sort()
        num2.sort()
        i = 0
        while i < len(num1):
            if num1[i] != num2[i]:
                return False
            else:
                i+=1
        return True
    return False

def main ():
    i = 1
    cont = True
    while (cont):
        if comp(i, i*2) and comp(i, i*3) and comp(i,i*4)and comp(i, i*5) and comp(i,i*6):
            print i
            cont = False
        i +=1

if __name__ == "__main__":
    main()

