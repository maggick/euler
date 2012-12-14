#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author : Matthieu Keller <keller.mdpa@gmail.com>
# answer : 932718654  with 9327

def concatenating (x,y,z):
    return int(str(x)+str(y)+str(z))

def isValide (xi):
    x = xi
    l = []
    while x >0:
        l.append(x%10)
        x/=10
    if len(l) !=9:
        return False
    l.sort()
    i = 0
    while i < len(l):
        if l[i] != i+1:
            return False
        i+=1
    return True

if __name__ == "__main__":
    n = 1
    res = 0
    while n < 9999:
        string = str(n)
        m = 1
        while len(string) < 10:
            m+=1
            string += str((n*m))
            if isValide(int(string)) and int(string)> res:
                res = int(string)
                print n, res
        n+=1
    print res
