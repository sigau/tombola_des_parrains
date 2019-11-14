#!/usr/bin/env python3
# -*- coding: utf-8 -*

import pygame as pg
from pygame.locals import *
import random , sys , re , os 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


var_local=str(os.getcwd())

#recupere les noms des photos
dir =var_local+"/photo_bcd"
liste_parrain=os.listdir(dir)

#liste a remplir pour pas tirer 2 fois un parrain 
parrain_tire=[]

img = mpimg.imread(var_local+"/background.jpg")


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


#initiation interface graphique 
pg.init()
fenetre = pg.display.set_mode((1920,1080), RESIZABLE)
clock = pg.time.Clock()

#mise en place du background
#fond = pg.image.load("background.png").convert()
#fenetre.blit(fond, (0,0))
font=pg.font.Font(None,32)

#mise en place de la name_box
input_box = pg.Rect(00, 00, 140, 32)
color_inactive = pg.Color(220, 20, 60)
color_active = pg.Color(255, 20, 147)
active = False
name = ''
done = False
pg.display.flip()


while not done :
	for event in pg.event.get() : 
		if event.type == pg.QUIT :
			done = True 
		if event.type == pg.MOUSEBUTTONDOWN :
			# si on clique avec la souris la boite réagis
			if input_box.collidepoint(event.pos):

				active = not active 
			else : 
				active = False
			#change la couleur de la boite
			color = color_active if active else color_inactive
		
		#on recupere ce qui est rentré 
		if event.type == pg.KEYDOWN : 
			if active :
				if event.key == pg.K_RETURN :
					### here come the tombola 
					print(name)
					name = ''
					t=random.sample(liste_parrain,1)
					if t not in parrain_tire :
						parrain_tire.append(t)
						print(t)
						photo= re.search("((\w).*(\w))",str(t))
						if photo :
							img= mpimg.imread(var_local+"/photo_bcd/"+str(photo.group(1)))
						plt.imshow(img)
						plt.show()
						

				#permet d'effacé le caractere
				elif event.key == pg.K_BACKSPACE:
					name = name[:-1]
				else: 
					name += event.unicode 


###tenter de remplacer fenetre par fond 
fenetre.fill((30, 30, 30))
# fait apparaitre le texte.
txt_surface = font.render(name, True, color)
# Resize the box if the text is too long.
width = max(200, txt_surface.get_width()+10)
input_box.w = width
# Blit the text.
fenetre.blit(txt_surface, (input_box.x+5, input_box.y+5))
# Blit the input_box rect.
pg.draw.rect(fenetre, color, input_box, 2)

pg.display.flip()
clock.tick(30)

pg.quit()
