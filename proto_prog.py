#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pygame as pg
from pygame.locals import *
import random , sys , re , os 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#recupere les noms des photos
dir ="/home/gautier/Bureau/photo_bcd"
dirIDS ="/home/gautier/Bureau/photo_ids"
dirPhymed="/home/gautier/Bureau/photo_phymed"
liste_parrain=os.listdir(dir)
liste_parrain_ids=os.listdir(dirIDS)
liste_parrain_phymed=os.listdir(dirPhymed)

#liste a remplir pour pas tirer 2 fois un parrain 
parrain_tire=[]

def main():
    screen = pg.display.set_mode((1920, 1080),RESIZABLE)
    pg.display.set_caption("Prog de depannage si personne n'a bosser dessus. Nan parce que en vrai sinon quelqu'un aurait changer le nom!")
    font = pg.font.Font(None, 32)
    police = pg.font.Font("/home/gautier/Bureau/tombola_des_parrains/Storyboo.TTF",72)
    texte = police.render("Soiree parrainage BCD 2019",True,pg.Color("lightskyblue3"))
    rectScreen = screen.get_rect()
    rectTexte = texte.get_rect()
    rectTexte.center = rectScreen.center
    clock = pg.time.Clock()
    input_box = pg.Rect(820, 600, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    logo_BCD = pg.image.load("/home/gautier/Bureau/tombola_des_parrains/Logo_BCD.png").convert_alpha()
    small_bcd=pg.transform.scale(logo_BCD, (364, 364)) 
    position_BCD=(750,50)
    logo_IDS = pg.image.load("/home/gautier/Bureau/tombola_des_parrains/Logo_IDS_Negatif.png").convert_alpha()
    small_ids=pg.transform.scale(logo_IDS, (283, 273)) 
    position_IDS=(400,150)
    logo_phymed = pg.image.load("/home/gautier/Bureau/tombola_des_parrains/Logo_Phymed_negatif.png").convert_alpha()
    small_phymed=pg.transform.scale(logo_phymed, (273, 273)) 
    position_phymed=(1200,150)



    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        parcours=re.search("((\w*)\s(.*))",str(text))
                        text =""
                        if ((parcours.group(2)=="BCD") or (parcours.group(2)=="bcd")):
                            t=random.sample(liste_parrain,1)
                            print("BCD test")

                            if t in parrain_tire : 
                                t=random.sample(liste_parrain,1)

                            if t not in parrain_tire :
                                parrain_tire.append(t)
                                
                                print(t)
                                photo=re.search("((\w).*(\w))",str(t))
                                if photo :
                                    img=mpimg.imread("/home/gautier/Bureau/photo_bcd/"+str(photo.group(1)))
                                plt.imshow(img)
                                plt.show()

                        if ((parcours.group(2)=="IDS") or (parcours.group(2)=="ids")):
                            t=random.sample(liste_parrain_ids,1)
                            print("ids test")

                            if t in parrain_tire:
                                t=random.sample(liste_parrain_ids,1)

                            if t not in parrain_tire :
                                parrain_tire.append(t)
                                    
                                print(t)
                                photo=re.search("((\w).*(\w))",str(t))
                                if photo :
                                    img=mpimg.imread("/home/gautier/Bureau/photo_ids/"+str(photo.group(1)))
                                plt.imshow(img)
                                plt.show()
                            
                        if ((parcours.group(2)=="phymed") or (parcours.group(2)=="Phymed")):
                            t=random.sample(liste_parrain_phymed,1)
                            print("phymed test")

                            if t in parrain_tire:
                                t=random.sample(liste_parrain_phymed,1)
                            
                            if t not in parrain_tire :
                                parrain_tire.append(t)
                                    
                                print(t)
                                photo=re.search("((\w).*(\w))",str(t))
                                if photo :
                                    img=mpimg.imread("/home/gautier/Bureau/photo_phymed/"+str(photo.group(1)))
                                plt.imshow(img)
                                plt.show()


                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        screen.blit(texte,rectTexte)
        screen.blit(small_bcd,position_BCD)
        screen.blit(small_ids,position_IDS)
        screen.blit(small_phymed,position_phymed)




        pg.display.flip()
        
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()

"""
list = ["Duffy Duck","Bart Simpson","Bender Bending Rodríguez","Gabriel García Márquez","Massimo Banzi","J. Johna Jameson"];
random.shuffle(list)
text = ""
for i in range(0,3):
    #print(list[i])
    text+=str("- " + list[i] + "\n")

print(text)
"""

#remplissage de la liste des parrain avec le fichier
"""
with open ("list_parrain.txt","r") as fichier :
    contenue=fichier.readlines()
    fichier.close
    for line in contenue :
        parrain=re.search("\s(\D*)\s(\D*)@",line) 
        if parrain : 
            liste_parrain.append(parrain.group(1))
print(liste_parrain)
"""