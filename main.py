import pygame
from pygame.locals import *
import time
import seconde
import commun
import random
import test
import poo
pygame.init()
pygame.event.get()
pygame.font.init()
fenetre = pygame. display. set_mode((0, 0), pygame. FULLSCREEN) 
screen = fenetre.get_size()
fond=pygame.image.load("background//place_village.png").convert_alpha()
fond = pygame.transform.scale(fond, (screen))
touche = pygame.key.get_pressed()
itour=['background//tour1.png','background//tour2.png','background//tour3.png','background//tour4.png']
imonstre={'orc':['bestiaire//autre//orc1.png','bestiaire//autre//orc2.png'],
          'zombie':['bestiaire//autre//zombie1.png','bestiaire//autre//zombie2.png'],
          'gobelin':['bestiaire//autre//gobelin1.png','bestiaire//autre//gobelin2.png','bestiaire//autre//gobelin2.png'],
          'squelette':['bestiaire//autre//squeletteepee1.png','bestiaire//autre//squeletteepee2.png'],
          'chauvesouris':['bestiaire//autre//chauvesouris1.png','bestiaire//autre//chauvesouris2.png'],
          'araigne':['bestiaire//autre//araigne1.png','bestiaire//autre//araigne1.png']}
nomontres=['orc','zombie','gobelin','squelette','chauvesouris','araigne']
choix=pygame.image.load("background//choix.png").convert_alpha()
choix = pygame.transform.scale(choix, (screen))
choix1=pygame.image.load("background//choix1.png").convert_alpha()
choix1 = pygame.transform.scale(choix1, (screen))
#song_background = pygame.mixer.music.load('thune.mp3')
#pygame.mixer.music.play(-1, 0.0, 0)
continuer=True
logo=pygame.image.load("background//logo.png").convert_alpha()
#logo=pygame.transform.scale(logo, (150, 163))
position=(0,0)
tour=0
orc1=poo.Orc()

while commun.continuer:
    time.sleep(0.01)
    if commun.accueil:
      print(screen[0],screen[1])
      fenetre.fill((0, 0, 0))
      fenetre.blit(logo, (300,200))
      seconde.quit(screen[0]-150,screen[1]-100,fenetre)
      seconde.play(screen[0]-320,screen[1]-300,fenetre,'Nouvelle Partie',"choix",0)
      seconde.play(screen[0]-150, screen[1]-200, fenetre, 'Crédit', "credit", 0)
    if commun.credit:
        fenetre.fill((0, 0, 0))
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1 == 0:
            fonte = pygame.font.Font('ressource//Dancing_Script//DancingScript-VariableFont_wght.ttf', 40)
            text = fonte.render('Programmeur/game designer : Mathis Cossard', True, (255, 255, 255), (0, 0, 0))
            fenetre.blit(text, (0, 0))
            text2 = fonte.render('Image : Loeiza', True, (255, 255, 255), (0, 0, 0))
            fenetre.blit(text2, (0, 100))
            seconde.play(0, screen[1]-50, fenetre, 'Retour', "accueil",1)
    if commun.choix:
        fenetre.fill((0,0,0))
        seconde.echap(screen[0] - screen[0] / 2, screen[1] - screen[1] / 2, fenetre, screen[0] - 25, 0)
        if commun.etat1 == 0:
            seconde.scroll('Kirito2.jpg', 60, screen, fenetre)
            fenetre.blit(choix, (0, 0))
            fenetre.blit(choix1, (0, 0))
            seconde.position()
            seconde.tour(0, 0, fenetre, "village", 'background//ruban1.png', screen, screen[0]-400, screen[1]-100, 260, 45)

    if commun.village:
        fenetre.blit(fond, (0,0))
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1==0:
            seconde.tour(0,0,fenetre,"tour",'background//tour_village1.png',screen,520,400,170,295)
            seconde.play(0, screen[1]-50, fenetre, 'Équipe', "equipe",0)
            seconde.play(0, screen[1]-150, fenetre, 'Inventaire', "inventaire",0)
            if touche:
                seconde.appuie("inventaire", pygame.K_i, "village",0)
                seconde.appuie("equipe", pygame.K_TAB, "village",1)

    if commun.tour:
        commun.raa=0
        commun.ebgyza=0
        tour=1
        seconde.imtour(itour,fenetre,screen)
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1==0:
            seconde.immonstre(imonstre,fenetre,nomontres,screen, 500, 0, 0)
            if touche:
                seconde.appuie("inventaire", pygame.K_i, "tour",0)
                seconde.appuie("equipe", pygame.K_TAB, "tour",1)
    if commun.equipe :
        fenetre.fill((0,0,0))
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1 == 0 and tour==0:
            seconde.play(0, screen[1]-50, fenetre, 'equipe', "village",1)
            seconde.appuie("equipe", pygame.K_TAB, "village",1)
        if commun.etat1 == 0 and tour==1:
            seconde.play(0, screen[1]-50, fenetre, 'equipe', "tour",1)
            seconde.appuie("equipe", pygame.K_TAB, "tour",1)
    if commun.inventaire:
        fenetre.fill((0, 0, 0))
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1 == 0 and tour==0:
            seconde.play(0, screen[1]-50, fenetre, 'inv', "village",0)
            seconde.appuie("inventaire",pygame.K_i,"village",0)
        if commun.etat1 == 0 and tour==1:
            seconde.play(0, screen[1]-50, fenetre, 'inv', "tour",0)
            seconde.appuie("inventaire",pygame.K_i,"tour",0)
    if commun.victoire:
        while commun.ebgyza==0:
            commun.lvl+=1
            orc1.get_lvl()
            orc1.modif_stat()  
            orc1.get_vie()
            print(commun.ebgyza)
            commun.ebgyza=1
        fenetre.fill((0,0,0))
        commun.imgm = 0
        commun.nmonstre=0
        commun.placem={}
        commun.gve=[]
        commun.monstres = []
        commun.nomonstre3=[]
        orc1.get_lvl()
        print(orc1)
        seconde.echap(screen[0]-screen[0]/2,screen[1]-screen[1]/2, fenetre, screen[0]-25, 0)
        if commun.etat1==0:
            seconde.play(screen[0]-320,screen[1]-300,fenetre,'Continuer',"tour",0)
    for event in pygame.event.get() :
        if event.type == QUIT :
            commun.continuer=False

    pygame.display.update()
pygame.quit()

1317, 940
1539, 941

1314, 965
1540, 975


1680
1920

(68, 555) (59, 1030)
(939, 562) (944, 1029)