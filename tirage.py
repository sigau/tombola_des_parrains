#!/usr/bin/env python3
# -*- coding: utf-8 -*

import random
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

j=0
liste_parrain=[]
liste=[i for i in range(10)]
img = mpimg.imread("/home/gautier/Bureau/parrain/background.jpg")

#on remplis la liste des parrains avec les nom precent dans le fichier
with open ("list_parrain.txt","r") as fichier :
    contenue=fichier.readlines()
    fichier.close
    for line in contenue :
        parrain=re.search("\s(\D*)\s(\D*)@",line) 
        if parrain : 
            liste_parrain.append(parrain.group(1))

tire=[]
print(len(liste_parrain))

while (j<len(liste_parrain)) : 
    t=random.sample(liste_parrain,1)
    if t not in tire :
        tire.append(t) 
        print(t)
        j=j+1

#print(liste_parrain)
plt.imshow(img)
plt.show()
