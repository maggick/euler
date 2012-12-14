# To change this template, choose Tools | Templates
# and open the template in the editor.

# project euler 74
# 5' minutes programm

__author__="matt"
__date__ ="$Apr 3, 2011 6:45:04 PM$"

def fact (n):
    c = 1
    res = 1
    while c < n+1:
        res *=c
        c+=1
    return res


def sumFact (n):
    res = 0
    i = 1
    tmp = n
    while (tmp >0):
        res += fact(tmp % 10)
        tmp = tmp / 10
    return res


res = 0
n = 10
while (n < 1000000):
    m = n
    if (m % 1000 == 0):
        print (m/1000)
    liste = list()
    liste.append(m)
    cont = 1
    while (cont):
        i=0
        m = sumFact(m)
        #print (m)
        liste.append(m)
        while (cont and i < len(liste)-1):
            if (liste[i] == m):
                cont = 0
            i+=1
    if (len (liste) - 1 == 60):
        res +=1
    n+=1
print (res)

