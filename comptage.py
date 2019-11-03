#!/usr/bin/Python
#-*- coding: utf-8 -*-

import sys, os, re      # module sys -> récup arguments ;
                        # os -> exécuter un exécutable ou créer une variable
                        #avec le resultat de l'executable

dico={"no_ext":0}
dir = sys.argv[1]

def parcours (dir) :
    #print 'Je suis dans ' + dir
    liste = os.listdir(dir)
    #print "liste :" + str(liste)

    for file in liste :
        chemin=dir+'/'+file
        if os.path.isdir(chemin) :                  # test si un fichier est un dossier
           #print "dossier trouvé :" + chemin
           parcours (chemin)
        else :                                        # le fichier est un fichier
           # print "fichier trouvé :" + chemin
           # ext = file.split('.')[-1]
            ext=re.search(".+\.(.+)",file)           #ext prend la valeur du der élém de dte
           #print "extension :" +  ext.group(1)
            if ext :             
               #ext="no_ext"
                if ext.group(1) in dico.keys():
                    dico[ext.group(1)] += 1
                else :
                    dico[ext.group(1)]=1
            else :
                dico["no_ext"]+=1
                

parcours (sys.argv[1])                         # appel initial de la fonction récursive 
print "extensions trouvées dans " + sys.argv[1] + " : \n\r" + str(dico)
print "Nombre total d'extensions :" + str(sum(dico.values()))
