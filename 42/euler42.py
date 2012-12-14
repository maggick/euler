# Resolution du probleme 42 du Projet Euler

__author__ = "matt"
__date__ = "$Nov 22, 2010 7:15:45 PM$"

#variables utiles
fichier = open("words.txt", "r")
contenu = fichier.read();
res = 0
i = 1
mot = ""
words = list()
max_length = 0

# lecture et stockage des mots dans une liste
# @type contenu str
while (i < len(contenu)-1):
    while (i < len(contenu) -1 and contenu[i + 1] != ','):
        mot += contenu[i]
        i += 1
    words.append(mot)
    if (len(mot) > max_length):
        max_length = len(mot)
    mot = ""
    i += 3
# on a plus besoin du fichier, on le ferme
fichier.close()

# calcul de la suite jusqu a un rend suffisant
suite = list()
suite.append(1)

i = 2
while (suite[len(suite)-1] < max_length * 25):
    suite.append(1.0/2 * i *(i+1))
    i+=1

# calcul de la somme des lettres de chaque mots
i = 0
convert = list()
while (i < len(words)):
    conv = 0
    j = 0
    while (j < len(words[i])):
        conv += (ord((words[i])[j])-64)
        j+=1
    convert.append(conv)
    i+=1

#on verifie si la somme d'un mot est dans la liste de la suite
i = 0
while (i < len(convert)):
    j = 0
    while (convert[i] > suite[j]):
        j+=1
    if (convert[i] == suite[j]):
        res +=1
    i+=1

print (res)
