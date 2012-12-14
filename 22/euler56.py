# projet euler, probleme 22
# name2.txt est le meme fichier que name.txt sauf trier par ordre alpabetique

__author__ = "matt"
__date__ = "$Nov 22, 2010 7:15:45 PM$"

#variables utiles
fichier = open("names2.txt", "r")
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
print(words)

print (len(words))
# on trie la liste par ordre alpha
i = 1
n = 0
while (i < len(words)-1):
    n = 0
    while (n < i):
    #comparaison alphabetique
        j = 0
        a_echanger = -1
        while (a_echanger == -1 and j < len(words[n]) and j < len(words[n + 1])):
            if (ord((words[n])[j]) > ord((words[n + 1])[j])):
                a_echanger = 1
            if (ord((words[n])[j]) < ord((words[n + 1])[j])):
                a_echanger = 0
            j += 1
        if (a_echanger == -1):
            if (len(words[n]) > len (words[n + 1])):
                a_echanger = 1
        if (a_echanger == 1):
            tmp = words[n]
            words[n] = words[n + 1]
            words[n + 1] = tmp
        n += 1
    i += 1
    print(i)

fichier = open("names2.txt", "w")
i = 0
fichier.write("\"")
while (i < len(words)-1):
    fichier.write(words[i] + "\",\"")
    i += 1
fichier.write(words[len(words)-1] + "\"")
print(words)

# calcul de la somme des lettres de chaque mots et on multiplie par la position
i = 0
convert = list()
while (i < len(words)):
    if (words[i] == "COLIN"):
        print (i)
    conv = 0
    j = 0
    while (j < len(words[i])):
        conv += (ord((words[i])[j])-64)
        j += 1
    convert.append(conv * (i + 1))
    i += 1

#on calcul la somme
i = 0
while (i < len(convert)):
    res += convert[i]
    i += 1

print (res)
# res = 871198282