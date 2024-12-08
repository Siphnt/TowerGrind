from typing import Tuple
import pygame
from pygame.locals import *
import commun
import time
import random
from PIL import Image
pygame.init()
pygame.event.get()

def position():
    position1 = (0,0)
    if pygame.mouse.get_pressed(num_buttons=3) == (True, False, False):
        position1 = pygame.mouse.get_pos()
        print(position1)



def quit(x,y,z) :
        position = (0, 0)
        position2 = (0, 0)
        fonte = pygame.font.Font('ressource//Permanent_Marker//PermanentMarker-Regular.ttf', 40)
        text = fonte.render('Quitter', True, (255, 255, 255), (0, 0, 0))
        z.blit(text, (x, y))
        if pygame.mouse.get_pressed(num_buttons=3)==(False,False,False):
            position=pygame.mouse.get_pos()
        if x<=position[0]<=x+140 and y<=position[1]<=y+30:
            fonte = pygame.font.Font('ressource//Permanent_Marker//PermanentMarker-Regular.ttf', 40)
            text = fonte.render('Quitter', True, (0, 0, 0), (255, 255, 255))
            z.blit(text, (x, y))
        if pygame.mouse.get_pressed(num_buttons=3)==(True,False,False):
            position2=pygame.mouse.get_pos()
        if x<=position2[0]<=x+140 and y<=position2[1]<=y+30:
                    commun.continuer=False

def play(x,y,z,o,p,u) :
    position = (0, 0)
    position2 = (0, 0)
    fonte = pygame.font.Font('ressource//Permanent_Marker//PermanentMarker-Regular.ttf', 40)
    text = fonte.render(o, True, (255, 255, 255))
    z.blit(text, (x, y))
    if pygame.mouse.get_pressed(num_buttons=3) == (False, False, False):
        position = pygame.mouse.get_pos()
    if x <= position[0] <= x + 300 and y <= position[1] <= y + 50:
        fonte = pygame.font.Font('ressource//Permanent_Marker//PermanentMarker-Regular.ttf', 40)
        text = fonte.render(o, True, (0, 0, 0), (255, 255, 255))
        z.blit(text, (x, y))
    if pygame.mouse.get_pressed(num_buttons=3) == (True, False, False):
        position2 = pygame.mouse.get_pos()
    if x <= position2[0] <= x + 300 and y <= position2[1] <= y + 50:
        commun.etatm = 0
        commun.etat1 = 0
        commun.etatour=0
        changeecran(p)
    if commun.etat2==1+u and x <= position2[0] <= x + 300 and y <= position2[1] <= y + 50:
        commun.etat2=0

def echap(x,y,z,a,b):
    touche = pygame.key.get_pressed()
    #print(commun.etat1)
    if commun.etat1==1:
        z.fill((0, 0, 0))
        quit(x,y,z)
        position = (100, 100)
        position2 = (500, 0)
        fonte = pygame.font.Font('freesansbold.ttf', 40)
        text = fonte.render('X', True, (255, 255, 255), (0, 0, 0))
        z.blit(text, (a, b))
        if pygame.mouse.get_pressed(num_buttons=3) == (False, False, False):
            position = pygame.mouse.get_pos()
        if a <= position[0] <= a + 140 and b <= position[1] <= b + 30:
            fonte = pygame.font.Font('freesansbold.ttf', 40)
            text = fonte.render('X', True, (0, 0, 0), (255, 255, 255))
            z.blit(text, (a, b))
        if pygame.mouse.get_pressed(num_buttons=3) == (True, False, False):
            position2 = pygame.mouse.get_pos()
        if a <= position2[0] <= a + 140 and b <= position2[1] <= b + 30:
            commun.etat1 = 0
    if touche[pygame.K_ESCAPE]==True and commun.etat1==1:
        time.sleep(0.1)
        commun.etat1= 0
    elif touche[pygame.K_ESCAPE]==True:
        time.sleep(0.1)
        commun.etat1=1

def tour(x,y,z,p,img,screen,x1,y1,x2,y2):
    img = pygame.image.load(img).convert_alpha()
    img = pygame.transform.scale(img, (screen))

    position = (0, 0)
    position2 = (0, 0)
    if pygame.mouse.get_pressed(num_buttons=3) == (False, False, False):
        position = pygame.mouse.get_pos()
    if x1 <= position[0] <= x1+x2 and y1 <= position[1] <= y1+y2:

        z.blit(img, (x, y))
    if pygame.mouse.get_pressed(num_buttons=3) == (True, False, False):
        position2 = pygame.mouse.get_pos()
    if x1 <= position2[0] <= x1+x2 and y1 <= position2[1] <= y1+y2:
        changeecran(p)

def imtour(list,z,screen):
    if commun.etatour==0:
        commun.imgtour = random.randint(0, len(list) - 1)
        commun.etatour = 1
    fond = pygame.image.load(list[commun.imgtour]).convert_alpha()
    fond = pygame.transform.scale(fond, (screen))
    z.blit(fond, (0, 0))

def immonstre(dict, z,list,screen,y,a,b):
    if commun.etat1 == 0:
        if commun.etatm == 0:
            commun.o = random.randint(1,5)
            for i in range(commun.o):
                commun.imgm = random.randint(0, 1)
                commun.nmonstre=random.randint(0,len(list)-1)
                commun.placem[commun.nmonstre]=dict[list[commun.nmonstre]][commun.imgm]
                commun.gve.append(dict[list[commun.nmonstre]][commun.imgm])                    
            for i in range(len(commun.gve)):
                if 'orc' in commun.gve[i] :
                    commun.nomonstre2['orc'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                if 'zombie' in commun.gve[i] :
                    commun.nomonstre2['zombie'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                if 'gobelin' in commun.gve[i] :
                    commun.nomonstre2['gobelin'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                if 'squelette' in commun.gve[i] :
                    commun.nomonstre2['squelette'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                if 'araigne' in commun.gve[i] :
                    commun.nomonstre2['araigne'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                if 'chauvesouris' in commun.gve[i] :
                    commun.nomonstre2['chauvesouris'+str(i)]=commun.gve[i]
                    commun.nbrmonstre.append(commun.nomonstre2)
                    commun.nomonstre2={}
                

            for dico in commun.nbrmonstre:
                for cle in dico:
                    commun.nomonstre3.append(cle)
                    monstre = pygame.image.load(dico[cle]).convert_alpha()
                    commun.nomonstre2[cle]=monstre
                    commun.monstres.append(commun.nomonstre2)
                    commun.nomonstre2={}
                    #print(commun.monstres)
        #print(commun.gve)
        touche = pygame.key.get_pressed()
        if commun.o>=1:
            z.blit(commun.monstres[0][commun.nomonstre3[0]], (screen[0]/2, screen[1]/2-200))
        #print(commun.o)
        if commun.o>=2:
            z.blit(commun.monstres[1][commun.nomonstre3[1]], (screen[0]/6, screen[1]/2-200))
        if commun.o>=3:
            z.blit(commun.monstres[2][commun.nomonstre3[2]], (screen[0]/12, screen[1]/2-200))
        if commun.o>=4:
            z.blit(commun.monstres[3][commun.nomonstre3[3]], (screen[0]/16, screen[1]/2-200))
        if commun.o>=5:
            z.blit(commun.monstres[-1][commun.nomonstre3[-1]], (screen[0]/20, screen[1]/2-200))
        if touche[pygame.K_m]==True:
            time.sleep(0.1)
            commun.nbrmonstre.pop(-1)
            commun.o-=1
        if commun.o==0:
            changeecran('victoire')
    commun.etatm = 1
    #print(test)
    #print(commun.nbrmonstre)
    #print(commun.monstres)
    #print(commun.placem)
    #print(commun.gve)
def taille(image):
    im = Image.open(image)
    commun.largeur = im.size[0]
    commun.hauteur = im.size[1]

def appuie(p,t,p2,u):
    touche = pygame.key.get_pressed()
    if commun.etat2==1+u:
        changeecran(p)
    if touche[t]==True and commun.etat2==1+u:
        time.sleep(0.1)
        commun.etat2= 0
        changeecran(p2)
    elif touche[t]==True:
        time.sleep(0.1)
        commun.etat2=1+u


def changeecran(text):
    if text == "accueil":
        commun.accueil = True
        commun.choix = False
        commun.village = False
        commun.tour = False
        commun.inventaire = False
        commun.equipe = False
        commun.credit=False
        commun.victoire=False
    elif text == "tour":
        commun.accueil = False
        commun.choix = False
        commun.village = False
        commun.tour = True
        commun.inventaire = False
        commun.equipe = False
        commun.victoire=False
    elif text == "inventaire":
        commun.accueil = False
        commun.choix = False
        commun.village = False
        commun.tour = False
        commun.inventaire = True
        commun.equipe = False
        commun.victoire=False
    elif text == "equipe":
        commun.accueil = False
        commun.choix = False
        commun.village = False
        commun.tour = False
        commun.inventaire = False
        commun.equipe = True
        commun.victoire=False
    elif text == "choix":
        commun.accueil = False
        commun.choix = True
        commun.village = False
        commun.tour = False
        commun.inventaire = False
        commun.equipe = False
        commun.victoire=False
    elif text == "village":
        commun.accueil = False
        commun.choix = False
        commun.village = True
        commun.tour = False
        commun.inventaire = False
        commun.equipe = False
        commun.victoire=False
    elif text == "credit":
        commun.accueil = False
        commun.choix = False
        commun.village = False
        commun.tour = False
        commun.inventaire = False
        commun.equipe = False
        commun.credit=True
        commun.victoire=False
    elif text=='victoire':
        commun.accueil = False
        commun.choix = False
        commun.village = False
        commun.tour = False
        commun.inventaire = False
        commun.equipe = False
        commun.credit=False
        commun.victoire=True






def scroll(image1,x,screen,fenetre):
    image = pygame.image.load(image1).convert()
    position = (0, 0)
    fenetre.blit(image,(x,commun.test))
    x1=55
    y1=550
    x2=940
    y2=1030
    print()
    if pygame.mouse.get_pressed(num_buttons=3) == (False, False, False):
        position = pygame.mouse.get_pos()
    if x1<position[0]<x2 and y1<position[1]<y2:
        for event in pygame.event.get():
            if event.type == MOUSEWHEEL:
                if event.y<0 and commun.test:
                    commun.test=commun.test-31
                    commun.limite=commun.limite-31
                if event.y>0 and commun.limite<450:
                    commun.test=commun.test+31
                    commun.limite=commun.limite+31
                    
                    
(412, 869)