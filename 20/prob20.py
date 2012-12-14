# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="matt"
__date__ ="$Oct 29, 2010 9:19:38 PM$"

i, res, n, fact = 1, 0, 100, 1
while (i< n+1):
    fact *=i
    i+=1
i=0
chaine = str(fact)
lenght = len(chaine)
while (i< lenght):
    res+=int(chaine[i:i+1])
    i+=1
print(res)