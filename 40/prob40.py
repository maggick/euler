# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="matt"
__date__ ="$Oct 29, 2010 9:31:19 PM$"

i, n = 1, 1000005
res = 1
ch = "0."
while (len(ch)<n):
    ch += str(i)
    i+=1
print(ch)
i = 1
while (i< 1000000):
    d = i+1
    i*=10
    res *=int(ch[d:d+1])
print(res)