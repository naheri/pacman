# -*- coding: utf-8 -*-

"""
Projet : ______4_________
Auteur : _AHAMADA Naheri______________
Date de création : ______________
Description : 

"""

#Modules importés


from textwrap import fill
from tkinter import *
import random
import json
from timeit import default_timer
import time
from tracemalloc import start
TK_SILENCE_DEPRECATION=1
from name import *
from graph2 import displayGraph

# ----------------------------------------------------------------
# Variables globales
# ----------------------------------------------------------------

#Liste des agents (ID)
agents=[]
#Liste des agents contaminés (ID) 
agents_vaccinés=[]
#Liste des états d'autonomie des agents (booleen)
sontAutonomes=[]
# liste des états de contamination (booleen)
sontContamines = [False,False,False,False,False,False]
contaminable = [True,True,True,True,True,True]
 # liste des agents contaminés (ID)
agents_contamines = []




#Coordonnées initiales
coordLInit_Agent=30#Largeur
coordHInit_Agent=30#Hauteur

#Coordonnées initiales des pièces:
coordLInit_Piece=15#Largeur
coordHInit_Piece=15#Hauteur

coordXInit=[]#Abscisse Agent
coordYInit=[]#Ordonnée Agent
coordXInit1=[]#Abscisse Agent2
coordYInit1=[]#Ordonnée Agent2

#informations pièces
couleur_piece="green"
nb_pieces=10
tabpieces=[]
RAYON_PIECE=4
coincounter=0 # nombre de pièces ramasées

#score & record
score_tot = 0
lastRecord = 0
# lancement : False si le jeu n'est pas lancé, Vrai si il est lancé
#launched = True
# temps écoulé
currentTime = 0
starttime = default_timer()
#Vitesses initiales
vitX=[]
vitY=[]
k=0


# liste qui gère l'état de fonctionnement==============================================================================
etat_fonc=[100,100,100,100,100,100]   #initialisés a 100%
etat_fonc_contamines = [100,100,100,100,100,100] #états de fonctionnement initialisés à 100%
#=====================================================================================================================



VIT_MAX_Joueur = 10       #5 #change vitesse du joueur non autonome
VIT_MAX_Autonome = 10     #5 #change vitesse du joueur autonome 

#Dimensions du canvas principal
LARG_CANVAS = 760
HAUT_CANVAS = 680
# Dimensions du canvas "étiquette"
LARG_ETIQUETTE = 100
HAUT_ETIQUETTE = 100
# dimensions d'une case d'un mur
LARG_CASE=40 #Largeur
HAUT_CASE=40 #Hauteur



#COULEUR_AUTO="orange"
COULEUR_NON_AUTO = "yellow"
COULEUR_COLLISION = "red"
COULEUR_MALADIE = "brown"
COULEUR_SCORE = "green"
#Couleur de la zone de vaccination
COULEUR_ZONE = "yellow"
#Couleur des agents contaminés
COULEUR_CONTAMINATION = "red"
#couleur de guérison
COULEUR_GUERISON =("blue") #Couleurs Agents    

#creation de différence couleur pour agents autonomes================================================================
COULEUR_AUTO=[]



# génère un nombre entier aléatoire 
n_agent_contamine = random.randint(3,6)
print(n_agent_contamine)
print("l'agent n°",n_agent_contamine,"est contaminé")
sontContamines = [False,False,False,False,False,False]
sontContamines[n_agent_contamine-1] = True





# appel de la fonction random pour générer des couleurs aléatoires
for etat in range(2,6):
    if sontContamines[etat]==False:
        COULEUR_AUTO.append("#%06x" % random.randint(0, 0xFFFFFF))
    else:
        COULEUR_AUTO.append(COULEUR_CONTAMINATION)
print(COULEUR_AUTO)
#====================================================================================================================
#Etat des animations et déplacements
etat_actif_depl_anim = False

#Demande d'arrêt
dde_arret = False
#arrêté ?(oui si = vrai, non si = false)
isLaunched = True
# tableau d'état de contamination

# tableau d'état de vaccination
print(sontContamines)
etat_vaccination = [False,False,False,False,False,False]
niveau1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2, 2, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ----------------------------------------------------------------
# Fonctions
# ----------------------------------------------------------------



"""
Obj: Tirage aléatoire d'un emplacement sans mur
Retour : liste de 2 élements : Coordonnées en pixel

"""
def getCoordAleatoiresSansMur():

    dispo=False
    while (not dispo):
        
        i=random.randint(0,len(niveau1)-1)
        j=random.randint(0,len(niveau1[0])-1)
        if (niveau1[i][j]==1 or niveau1[i][j]==2):
            dispo=True

    return [i*LARG_CASE+5,j*HAUT_CASE+5]



"""
Obj: Convertir les indices de tableau en coordonnées pixel 
Paramètres : indices du tableau niveau
Retour : liste des 2 coordonnées en pixel 
"""
def getConvertCoordPixelenCoordNiveau(i,j):
    x=5+LARG_CASE*i
    y=5+HAUT_CASE*j
    return [x,y]

"""
Obj: Convertir les coordonnées pixel en indices de tableau niveau
Paramètres : coordonnées pixel
Retour : liste des 2 indices du tableau niveau1
"""
def getConvertCoordPixelenCoordNiveau(x,y):
    i=int((x-5)/(LARG_CASE-((x-5)%LARG_CASE)))
    j=int((y-5)/(HAUT_CASE-((y-5)%HAUT_CASE)))
    #print(str(i)+"x"+str(j))
    return [i,j]

"""
Obj: Controler la disponibilité d'une zone
Retour : Entier
> 0 : Mur
> 1 : Rien
"""
def getOccupCoordNiveau1(x,y):
    coordNiveau=getConvertCoordPixelenCoordNiveau(x,y)
    return niveau1[coordNiveau[0],coordNiveau[1]]



"""
Création d'une zone de vaccination
"""
def creationZone():
    global zone_de_vaccination
    posInitZone=getCoordAleatoiresSansMur()
    zone_de_vaccination=gestionCanvas.create_rectangle(LARG_CASE, HAUT_CASE,LARG_CASE, HAUT_CASE, fill="pink", outline="")
"""
Obj: Gestion des évènements du clavier

"""
def evenements(event):

    if event.keysym=="Up":
        demarrage(0,-VIT_MAX_Joueur,btnHaut)
    elif event.keysym=="Down":
        demarrage(0,VIT_MAX_Joueur,btnBas)
    elif event.keysym=="Left":
        demarrage(-VIT_MAX_Joueur,0,btnGauche)
    elif event.keysym=="Right":
        demarrage(VIT_MAX_Joueur,0,btnDroite)

    

    #boutons de contrôle WASD ==================================================================================================================      
    if event.keysym=="Z":
        demarrage2EME(0,-VIT_MAX_Joueur,Z)
    elif event.keysym=="S":
        demarrage2EME(0,VIT_MAX_Joueur,S)
    elif event.keysym=="Q":
        demarrage2EME(-VIT_MAX_Joueur,0,Q)
    elif event.keysym=="D":
        demarrage2EME(VIT_MAX_Joueur,0,D)
    #=====================================================================================================================================


    elif event.keysym=="Escape":
        arret()
    elif event.keysym=="space":
        depart()


 
"""
Obj: Réinitialisation des couleurs des boutons

"""
def init_couleurs():
    btnDroite.config(bg="black")
    btnGauche.config(bg="black")
    btnHaut.config(bg="black")
    btnBas.config(bg="black")

    # Definir les couleur des boutons secondaires ==========================================================================================
    D.config(bg="black")
    Q.config(bg="black")
    Z.config(bg="black")
    S.config(bg="black")
    #=======================================================================================================================================


    
    btnInit.config(bg="red")
    btnArret.config(bg="red")



 
"""
Obj: Instanciation d'un nouvel Agent
Param : true si l'on souhaite créer un agent autonome
"""
def creationAgent(pEstAutonome):
    global vitX,vitY,coordXInit,coordYInit,agents,sontAutonomes,n_agent_contamine
    
    posInitAgent=getCoordAleatoiresSansMur()
    coordXInit.append(posInitAgent[0])
    coordYInit.append(posInitAgent[1])
    posInitAgent1=getCoordAleatoiresSansMur()
    coordXInit1.append(posInitAgent1[0])
    coordYInit1.append(posInitAgent1[1])
    vitX.append(0)
    vitY.append(0)
    if (pEstAutonome):
        
        agents.append(gestionCanvas.create_arc(coordXInit[i],coordYInit[i],
                                        coordXInit[i]+coordLInit_Agent,coordYInit[i]+coordHInit_Agent,
                                        fill=COULEUR_AUTO[i],start=15,extent=330))    
                    
    else:
        
        agents.append(gestionCanvas.create_arc(coordXInit1[i],coordYInit1[i],
                                        coordXInit1[i]+coordLInit_Agent,coordYInit1[i]+coordHInit_Agent,
                                        fill=COULEUR_NON_AUTO,start=15,extent=330))
    sontAutonomes.append(pEstAutonome)

"""
Fonction s'occupant de la création de pièces
"""
def creationPieces():
    posInitPieces=getCoordAleatoiresSansMur()
    tabpieces.append(gestionCanvas.create_oval(posInitPieces[0]+(LARG_CASE-RAYON_PIECE)/5,posInitPieces[1]+(HAUT_CASE-RAYON_PIECE)/5, posInitPieces[0]+RAYON_PIECE+(LARG_CASE-RAYON_PIECE)/2, posInitPieces[1]+RAYON_PIECE+(LARG_CASE-RAYON_PIECE)/2, fill = couleur_piece))
 


"""
Obj: Démarrage des déplacements du Joueur et de l'Agent autonome
Param :
    pVitesseX : Vitesse demandée par le joueur sur l'axe des abcisses
    pVitesseY : Vitesse demandée par le joueur sur l'axe des ordonnées
    pBtn : Bouton utilisé dont l'apparence doit mise à jour
"""
def demarrage(pVitesseX,pVitesseY, pBtn):
    
    #Utilisation des variables globales (non locale) >> pas de réinitialisation à chaque appel
    global etat_actif_depl_anim, vitX, vitY

    for i in range(len(sontAutonomes)):
        if not sontAutonomes[i] and i == 0:    # À condition que ce soit le premier agent====================================================
            vitX[i]=pVitesseX
            vitY[i]=pVitesseY

    
    #Couleur des boutons utilisés
    init_couleurs()
    pBtn.config(bg="blue")

    dde_arret = False
    
    if etat_actif_depl_anim == False :
        deplacements()


# Ajouter une deuxième fonction pour controler le 2ème agent avec les touches ZQSD==============================================================

def demarrage2EME(pVitesseX,pVitesseY, pBtn):
    
    #Utilisation des variables globales (non locale) >> pas de réinitialisation à chaque appel
    global etat_actif_depl_anim, vitX, vitY

    for i in range(len(sontAutonomes)):
        if not sontAutonomes[i] and i != 0:
            vitX[i]=pVitesseX
            vitY[i]=pVitesseY

    
    #Couleur des boutons utilisés
    init_couleurs()
    pBtn.config(bg="blue")

    dde_arret = False
    
    if etat_actif_depl_anim == False :
        deplacements()

#================================================================================================================================================

"""
Obj: Lancement de tous les déplacements
"""
def deplacements():

    global etat_actif_depl_anim, dde_arret
    
    i=0
    for noAgent in range(len(agents)):
        deplacement(noAgent,sontAutonomes[i],etat_fonc)
        i+=1
    if dde_arret == False :#Tant que le jeu ne doit pas être arrêté
        fen_princ.after(100, deplacements)#Patienter 100ms afin d'appeler à nouveau cette même fonction (récursivité)
    else:
        dde_arret = False #Arrêt pris en compte et réinitialisé
        etat_actif_depl_anim = False #Animation désactivée
        

"""
Obj: Gestion des déplacements de tous agents

"""
def deplacement(pNoAgent, pAutonomie, etat_fonc):
    global agents, vitX, vitY, murs,k,score_tot, coincounter, currentTime, lastRecord
    global etat_actif_depl_anim
    
    #Initialisation
    etat_actif_depl_anim = True
    mod_angle = 0
    # Record précédent 
    record.itemconfigure(vrairecord, text="\n %d" %getHighScore())
    # temps actuel
    currentTime =int(default_timer() - starttime)
    temps.itemconfigure(vraitemps, text="\n%d" %currentTime)
    #Récupération des coordonnées de l'agent
    coordActuelles = gestionCanvas.coords(agents[pNoAgent])


    #Liste des éléments présents dans la zone devant le Joueur (anticipation en fonction de la direction de la vitesse)
    liste_obstacles = gestionCanvas.find_overlapping(coordActuelles[0]+vitX[pNoAgent],coordActuelles[1]+vitY[pNoAgent],
                                                     coordActuelles[2]+vitX[pNoAgent],coordActuelles[3]+vitY[pNoAgent])
    collision_zone_de_vaccination = False 
    collisionPiece = False #vrai si le joueur entre en collision avec une pièce
    collisionAutonome = False #Vrai si le joueur s'apprête à entrer en collision avec un agent autonome
    collisionMur = False #Vrai si le joueur s'apprête à entrer en collision avec un mur
    collisionAgentContamine = False #Vrai si le joueur s'apprête à entrer en collision avec un agent contaminé

    if len(liste_obstacles) > 0 :#Détection de l'obstacle

        for obs in liste_obstacles : #Parcours de la liste des entités présentes dans la zone

            if obs != agents[pNoAgent] : #Collision du joueur avec un autre : mur ou agent autonome ou pièces ou agent contaminé ? 
                # vérifier si l'obstacle est une zone de vaccination
                z = 0
                while (z<len(zone_de_vaccination) and collision_zone_de_vaccination == False):
                    if obs == zone_de_vaccination[z]:
                        collision_zone_de_vaccination = True #  détection d'une zone de vaccination
                        gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_GUERISON)
                        print("collision de l'agent",pNoAgent,"avec une zone de vaccination" )
                    else : 
                        z+=1
 
                #Vérifier si obs est un mur
                m = 0
                while ( m<len(murs) and collisionMur==False):
                    if obs == murs[m]:
                        collisionMur=True #Collision avec un mur détectée 
                        print("collision de l'agent",pNoAgent,"avec un mur")
                    else:
                        m=m+1
                v = 0
                while ( v<len(agents_contamines) and collisionAgentContamine==False):
                    if obs == agents_contamines[v]:
                        collisionAgentContamine=True #Collision avec un agent contaminé détectée
                        print("collision de l'agent",pNoAgent,"avec un agent contaminé")
                        if etat_vaccination[pNoAgent] == False:
                            # le rajouter à la liste des agents contaminés si il n'y est pas déjà
                            if agents_contamines.count(agents[pNoAgent]) == 0:
                                sontContamines[pNoAgent] = True # l'agent devient contaminé si il n'est pas vacciné
                                agents_contamines.append(agents[pNoAgent])
                            gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_MALADIE)
                        else:
                            print("l'agent",pNoAgent,"est vacciné et ne peut pas être contaminé")
                    else:
                        v=v+1

                    #vérifier si obs est un agent autonome 
                if (not collisionMur and not collision_zone_de_vaccination and not collisionPiece):
                    collisionAutonome = True

                    #vérifier si obs est une pièce
                    if (not collisionAutonome and not collisionMur and not collision_zone_de_vaccination and not collisionAgentContamine):
                        collisionPiece = True
                        print("collision avec une pièce")

    # si l'agent n'est pas vacciné ET contaminé, son état de santé diminue de 0.2 régulièrement
    if sontContamines[pNoAgent] == True and etat_vaccination[pNoAgent] == False:
        gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_MALADIE)
        print("l'état de fonctionnement de l'agent",pNoAgent,"diminue de 0.2")
        etat_fonc[pNoAgent] = etat_fonc[pNoAgent] - 0.2
    if collisionAgentContamine == True:
        gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_MALADIE)
     #Inclure les couleurs choisies pour revenir à la couleur initiale apres collision selon le numero de l'agent autonome [2 3 4 5] vu que les deux premiers sont non autonomes============================================  
    elif (pAutonomie and pNoAgent):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[0])

    elif (pAutonomie and pNoAgent == 3):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[1])

    elif (pAutonomie and pNoAgent == 4):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[2])

    elif (pAutonomie and pNoAgent == 5):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[3])

    else :
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_NON_AUTO) #COULEUR_NON_AUTO)
    # Si l'agent est en collision avec un la zone de vaccination il ne peut plus être contaminé
    if collision_zone_de_vaccination == True:
        etat_vaccination[pNoAgent] = True
        gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_GUERISON)
        if sontContamines[pNoAgent] == True:
            sontContamines[pNoAgent] = False
            agents_contamines.remove(agents[pNoAgent])
        print("L'agent ",pNoAgent,"est immunisé, il arrête de perdre de l'état de fonctionnement")
     #Inclure les couleurs choisies pour revenir à la couleur initiale apres collision selon le numero de l'agent autonome [2 3 4 5] vu que les deux premiers sont non autonomes============================================  
    elif (pAutonomie and pNoAgent):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[0])

    elif (pAutonomie and pNoAgent == 3):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[1])

    elif (pAutonomie and pNoAgent == 4):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[2])

    elif (pAutonomie and pNoAgent == 5):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[3])

    else :
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_NON_AUTO) #COULEUR_NON_AUTO)

    if collisionAutonome == True: # Changement de la couleur de l'agent si il est en collision
        if pNoAgent == 0 or pNoAgent == 1 :
            gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_COLLISION) 
            etat_fonc[pNoAgent] -= 2
            print("L'état de l'agent ",pNoAgent,"est à ", etat_fonc[pNoAgent])

    #Inclure les couleurs choisies pour revenir à la couleur initiale apres collision selon le numero de l'agent autonome [2 3 4 5] vu que les deux premiers sont non autonomes============================================  
    elif (pAutonomie and pNoAgent):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[0])

    elif (pAutonomie and pNoAgent == 3):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[1])

    elif (pAutonomie and pNoAgent == 4):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[2])

    elif (pAutonomie and pNoAgent == 5):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[3])

    else :
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_NON_AUTO) #COULEUR_NON_AUTO)
    pieces = 0
    if not sontAutonomes[pNoAgent] : 
        while ( pieces<len(tabpieces) and collisionPiece==False):
            if obs == tabpieces[pieces]:
                collisionPiece = True#Collision avec une pièce detectée 
                gestionCanvas.itemconfig(agents[pNoAgent], fill = COULEUR_SCORE) # changement de la couleur de l'agent
                gestionCanvas.delete(fen_princ, tabpieces[pieces]) #Suppresion de la pièce après avoir été touchée 
                score_tot = score_tot + 5
                coincounter = coincounter + 1
                #actualisation du canvas "score"
                scoreCanvas.itemconfigure(vraiscore, text=("\n %d" %score_tot))
               
                #actualisation du canvas "nombre de pièces"
                nbpieces.itemconfigure(vrainbpieces, text=("\n %d" %coincounter))
                print("le score total est maintenant de ", score_tot)
            else:
                pieces+=1  

     #Inclure les couleurs choisies  pour revenir à la couleur initiale apres collision selon le numero de l'agent autonome [2 3 4 5] vu que les deux premiers sont non autonomes============================================  
    elif (pAutonomie and pNoAgent == 2):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[0])

    elif (pAutonomie and pNoAgent == 3):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[1])

    elif (pAutonomie and pNoAgent == 4):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[2])

    elif (pAutonomie and pNoAgent == 5):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_AUTO[3])
        #====================================================================================================================================================================================================================


    else :
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_NON_AUTO) #COULEUR_NON_AUTO)

        
    if (pAutonomie and pNoAgent == 6):
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_CONTAMINATION)
    if collisionMur :#Stopper l'agent
        vitX[pNoAgent]=0
        vitY[pNoAgent]=0

    else :  


        # Verifier si l'etat de fonctionnement des agents est egale a 0====================================================
        if etat_fonc[pNoAgent] <= 0 :
        
            vitX[pNoAgent]=0  #immobiliser l'agent
            vitY[pNoAgent]=0
            #arret()
            if etat_fonc[pNoAgent] <= 0 :   # si le deuxième agent est immobilisé, arret du jeu
                arret()
                gestionCanvas.create_text(HAUT_CANVAS/2, LARG_CANVAS/2, text="LE JEU EST TERMINÉ!!!", font=('Helvetica 50 bold'), fill="red")
                print ('Game Over: tous les agents sont immobilisés')

        #=================================================================================================================


        else:

            if (vitX[pNoAgent] <0 or vitY[pNoAgent]>0) :#Rotation de la représentation de l'agent en cas de changement de sens
                mod_angle = 180

        
            if (vitX[pNoAgent]!=0 or vitY[pNoAgent]!=0):
                #Affichage de l'agent en sens direction horizontale comme un cercle incomplet de 30 à 360° ou de 15 à 330°
                if vitY[pNoAgent] == 0 :
                    
                        if (gestionCanvas.itemcget(agents[pNoAgent], 'start') == '15.0' or gestionCanvas.itemcget(agents[pNoAgent], 'start') == '195.0' ) :
                            gestionCanvas.itemconfig(agents[pNoAgent], start=30+mod_angle, extent=300)
                        else:
                            gestionCanvas.itemconfig(agents[pNoAgent], start=15+mod_angle, extent=330)



                #Affichage de l'agent en sens direction verticale comme un cercle incomplet de 120 à 300° ou de 105 à 330°
                if vitX[pNoAgent] ==0 :
                    

                    if (gestionCanvas.itemcget(agents[pNoAgent], 'start') == '105.0' or gestionCanvas.itemcget(agents[pNoAgent], 'start') == '285.0') :
                        gestionCanvas.itemconfig(agents[pNoAgent], start=120+mod_angle, extent=300)
                    else:
                        gestionCanvas.itemconfig(agents[pNoAgent], start=105+mod_angle, extent=330)



                # placement de l'agent
                gestionCanvas.move(agents[pNoAgent],vitX[pNoAgent],vitY[pNoAgent])
    

    if (pAutonomie):

            #Tirage aléatoire d'un pourcentage de la direction
            direction = random.randint(1,100)

            if (vitX[pNoAgent]==0 and vitY[pNoAgent]==0): #Changement de direction si nous sommes à l'arrêt
                if direction <= 25 :#25% de chance qu'il parte à droite
                    vitX[pNoAgent] = VIT_MAX_Autonome
                    vitY[pNoAgent] = 0

                elif direction <= 50 :#25% de chance qu'il parte à gauche
                    vitX[pNoAgent] = -VIT_MAX_Autonome
                    vitY[pNoAgent] = 0

                elif direction <= 75 :#25% de chance qu'il parte vers le bas
                    vitX[pNoAgent] = 0
                    vitY[pNoAgent] = VIT_MAX_Autonome

                else:# de 75% et 100% inclus
                    vitX[pNoAgent] = 0#25% de chance qu'il parte vers haut
                    vitY[pNoAgent] = -VIT_MAX_Autonome
    
    """
    Arrêt de la partie lorsqu'il n'y a plus de pièces, écriture du score
    """

    if score_tot == 50: # lorsque le score est au maximum, le jeu est fini, j'enregistre le score dans un fichier texte
        arret()

    return score_tot, currentTime

def getScores():
    # Open the text file
    scores = []
    with open('scores.txt', 'r') as f:
        # Read the contents of the file
        contents = f.read()
        print(contents)
        # Split the string into a list of lines
        lines = contents.split('\n')
        print(lines)
        # Initialize a variable to store the highest score
        highest_score = 0
        # Iterate over the list of lines
        for line in lines:
            # Split the line into a list of words
            words = line.split()
            scores.append(score = words[2])
    return scores

'''
    Fonction qui permet de sauvegarder le score dans un fichier texte'''

def writeScore():
    with open("scores.txt", "a") as f:
        f.write("\n"+str(name_input)+ " score: "+str(score_tot))

"""Obj: get high score from file"""
def getHighScore():
    # Open the text file
    with open('scores.txt', 'r') as f:
        # Read the contents of the file
        contents = f.read()
        print(contents)
        # Split the string into a list of lines
        lines = contents.split('\n')
        print(lines)
        # Initialize a variable to store the highest score
        highest_score = 0
        # Iterate over the list of lines
        for line in lines:
            # Split the line into a list of words
            words = line.split()
            highest_score = max(highest_score, int(words[2]))
    return highest_score
"""
Obj: Réinitialisation toutes les positions et les vitesses et arrêt des animations et déplacements
"""
def depart():

    global vitX, vitY, starttime, lastRecord
    record.itemconfigure(vrairecord, text="%d" %lastRecord)
    #Mise à jour des boutons
    init_couleurs()
    btnInit.config(bg="blue")

    #Annulation de la vitesse en cours
    for i in range (len(vitX)):
        vitX[i]=0
    for i in range (len(vitY)):
        vitY[i]=0

    #Arrêt des animations et des déplacements
    arret()
    # initialisation du temps écoulé
    starttime = default_timer()
    #Repositionnement aux valeurs initiales
    i=0
    for a in agents:
        gestionCanvas.coords(a,coordXInit[i],coordYInit[i],
                             coordXInit[i]+coordLInit_Agent,coordYInit[i]+coordHInit_Agent)
        gestionCanvas.itemconfig(a, start=15,extent=330)
        i=i+1

"""
Obj: Arrêt des animations et déplacements sans repositionner
"""
def arret():
    global dde_arret,isLaunched, score_tot
        
    #Mise à jour des boutons
    init_couleurs()
    btnArret.config(bg="blue")
    isLaunched = False
    #Mise à jour de la variable globale utilisée dans les déplacements
    dde_arret = True
    # ouverture du fichier texte à la fin de la partie
    print(agents)
    print(agents_contamines)
    print(sontContamines)
    print(etat_vaccination)
    writeScore()
    # affichage de l'évolution du score
    
'''restart everything'''
def restart():
    global score_tot,temps
    score_tot = 0
    depart()
    # on remet les variables à 0
    for i in range (len(etat_vaccination)):
        etat_vaccination[i] = False
    for i in range (len(agents_contamines)):
        agents_contamines[i] = False
    for i in range (len(sontContamines)):
        sontContamines[i] = False

# ----------------------------------------------------------------
# Corps du programme
# ----------------------------------------------------------------

#Paramétrage de la fenêtre principale
fen_princ = Tk()
fen_princ.title("PACAGENT L1 SPI")
fen_princ.geometry("900x700")#Dimensions de la fenêtre
fen_princ.bind("<Key>",evenements)#Définition de la fonction de gestion des évènements clavier

#Paramétrage du Canvas
gestionCanvas = Canvas(fen_princ, width=LARG_CANVAS, height=HAUT_CANVAS, bg='ivory', bd=0, highlightthickness=0)
gestionCanvas.grid(row=0,column=0, padx=10,pady=10)

# paramétrage du canvas score "étiquette" (carré)

scoreCanvas = Canvas(fen_princ, width=LARG_ETIQUETTE, height=HAUT_ETIQUETTE, bg='ivory', bd=0, highlightthickness=0, background="blue")
motscore = scoreCanvas.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("SCORE \n") ,font = "Arial 20 italic",fill="yellow", anchor="center")
vraiscore = scoreCanvas.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("\n %d" %score_tot) ,font = "Arial 20 italic",fill="yellow", anchor="center")

scoreCanvas.place(x=782,y=545)

# paramétrage du canvas nombre de pièces ramassé "étiquette" (carré)

nbpieces = Canvas(fen_princ, width=LARG_ETIQUETTE, height=HAUT_ETIQUETTE, bg='ivory', bd=0, highlightthickness=0, background="blue")
txtnbpieces =  nbpieces.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("PIECES \n") ,font = "Arial 20 italic",fill="yellow", anchor="center")
vrainbpieces = nbpieces.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("\n %d" %coincounter) ,font = "Arial 20 italic",fill="yellow", anchor="center")

nbpieces.place(x=782,y=443)

    
# paramétrage du canvas ("temps")


temps = Canvas(fen_princ, width=LARG_ETIQUETTE, height=HAUT_ETIQUETTE, bg='ivory', bd=0, highlightthickness=0, background="blue")
txttemps =  temps.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("TEMPS \n") ,font = "Arial 20 italic",fill="yellow", anchor="center")
vraitemps = temps.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("\n 0s") ,font = "Arial 20 italic",fill="yellow", anchor="center")

temps.place(x=782,y=20)
# paramétrage du canvas ("record")


record = Canvas(fen_princ, width=LARG_ETIQUETTE, height=HAUT_ETIQUETTE, bg='ivory', bd=0, highlightthickness=0, background="blue")
txtrecord =  record.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("RECORD \n") ,font = "Arial 20 italic",fill="yellow", anchor="center")
vrairecord = record.create_text(LARG_ETIQUETTE/2,HAUT_ETIQUETTE/2,text=("\n %d" %getHighScore()) ,font = "Arial 20 italic",fill="yellow", anchor="center")

record.place(x=782,y=123)




#Affichage des murs du niveau 1
murs=[]
zone_de_vaccination = []
for i in range(len(niveau1)):
    for j in range(len(niveau1[i])):
        if (niveau1[i][j]==0):
            murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="blue", outline=""))
            #affichage zone de vaccination
        if (niveau1[i][j]==2):
            zone_de_vaccination.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="pink", outline=""))
        

#Affichage des agents gérés par l'utilisateur
nbAgentNonAutonomes=2
for i in range(nbAgentNonAutonomes):
    creationAgent(False)

#Affichage des agents autonomes
nbAgentAutonomes=4
for i in range(nbAgentAutonomes):
    creationAgent(True)

for i in range(nb_pieces):
    creationPieces()

# get score
with open('scores.txt', 'r') as f:
    score = f.read()
    score = score.split(':')
    print(score[1])

# affiche les agents
agents_contamines.append(agents[n_agent_contamine-1]) # ajout d'un agent autonomen choisi aléatoirement dans la liste des agents contamines
print(agents)
print(agents_contamines)
print(etat_vaccination)

#Zone dédiée aux boutons
zoneBtn = Frame(fen_princ)
zoneBtn.grid(row=0,column=1,ipadx=5)


#Zone dédiée aux boutons secondaires =======================================================================================================
zoneBtn1 = Frame(fen_princ)
zoneBtn1.grid(row=0,column=2,ipadx=5)
#==========================================================================================================================================

#Boutons directionnels 
btnDroite = Button(zoneBtn, text=">>>", fg="black", bg="black",relief=SUNKEN, command=lambda: demarrage(VIT_MAX_Autonome,0,btnDroite))
btnDroite.pack(fill=X)

btnGauche = Button(zoneBtn, text="<<<", fg="black", bg="black", relief=SUNKEN,command=lambda:demarrage(-VIT_MAX_Autonome,0,btnGauche))
btnGauche.pack(fill=X)

btnHaut = Button(zoneBtn, text="^^^", fg="black", bg="black",relief=SUNKEN, command=lambda:demarrage(0,-VIT_MAX_Autonome,btnHaut))
btnHaut.pack(fill=X)

btnBas = Button(zoneBtn, text="vvv", fg="black", bg="black",relief=SUNKEN, command=lambda:demarrage(0,VIT_MAX_Autonome,btnBas))
btnBas.pack(fill=X)




#Boutons directionnels secondaires=======================================================================================================
D = Button(zoneBtn1, text="D", fg="black", bg="black",relief=RAISED, command=lambda:demarrage2EME(VIT_MAX_Autonome,0,D))
D.pack(fill=X)

Q = Button(zoneBtn1, text="Q", fg="black", bg="black",relief=RAISED, command=lambda:demarrage2EME(-VIT_MAX_Autonome,0,Q))
Q.pack(fill=X)

Z = Button(zoneBtn1, text="Z", fg="black", bg="black",relief=RAISED, command=lambda:demarrage2EME(0,-VIT_MAX_Autonome,Z))
Z.pack(fill=X)

S = Button(zoneBtn1, text="S", fg="black", bg="black",relief=RAISED, command=lambda:demarrage2EME(0,VIT_MAX_Autonome,S))
S.pack(fill=X)

#=========================================================================================================================================

#Boutons d'arrêt et de réinitialisation
btnArret = Button(zoneBtn, text="STOP", fg="black", bg="red", command=arret)
btnArret.pack(fill=X)
showGraph = Button(zoneBtn, text="show Graph", fg="black", bg="red", command=displayGraph)
showGraph.pack(fill=X)
btnInit = Button(zoneBtn, text="INIT", fg="black", bg="red", command=depart)
btnInit.pack(fill=X)
print(sontAutonomes)
'''# Coordonnées de la position de la souris
def callback(e):
   x= e.x
   y= e.y
   print("Coords pointeur : %dx, %dy" %(x,y))
fen_princ.bind('<Motion>',callback)'''
#Rafraichissement de la fenêtre et de tout son contenu
fen_princ.mainloop() 
