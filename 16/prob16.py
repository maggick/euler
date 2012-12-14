# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="matt"
__date__ ="$Oct 29, 2010 9:09:00 PM$"

i, res, dev, puiss = 0, 0, 2, 1000
while (i < puiss -1):
    dev *= 2
    i +=1
print(dev)
chaine=str(dev)
length = len(chaine)
i = 0
while (i < length):
    res +=int(chaine[i:i+1])
    i+=1
print(res)
