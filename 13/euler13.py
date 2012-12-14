# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="matt"
__date__ ="$Oct 29, 2010 8:31:43 PM$"

fichier = open("numbers", "r")
chaine = fichier.read()
i = 0
res = 0
while (i<100):
    ch = chaine[(50*i)+i:(i+1)*50+i]
    res += long(ch)
    i+=1
#    print(ch)
#    print(res)
print ("res : \n")
print(str(res)[0:10])

