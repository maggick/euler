# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="matt"
__date__ ="$Nov 18, 2010 5:34:55 PM$"

j = 1
res = 0
k = 0
temp = 0
i=0
n = 1
while (i <999):
    n*=10
    i+=1
print (n)
# dix puissance deux donne deux digits
while (res / n < 1):
#while (res / 10^999 <1)
    temp = res
    res += j
    j = temp
    k+=1
print(res)
print (k)