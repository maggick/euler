# To change this template, choose Tools | Templates
# and open the template in the editor.

#Project Euler, prob 15
#Starting in the top left corner of a 2×2 grid,
#there are 6 routes (without backtracking) to the bottom right corner.
#How many routes are there through a 20×20 grid?
#answer : 137846528820


__author__="matt"
__date__ ="$Jan 7, 2011 9:38:19 PM$"

n = 20

tab = []
list = []

i = 0
tmp1 = []
while (i <=n):
    j=0
    list=[]
    #print tab
    while (j <= n):
        if (j == 0 or i == 0):
            list.append(1)
        if (j != 0 and i != 0): #and j != i
            list.append(tmp[j] + list[j-1])
#        if (i == j):
#            list.append(list[j-1])
        j+=1
    i+=1
    tab.append(list)
    tmp = list

print tab[n][n]