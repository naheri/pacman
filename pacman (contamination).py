#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Projet : ______4_________
Auteur : _AHAMADA Naheri______________
Date de création : ______________
Description : 

"""

#Modules importés
from tkinter import *
import random
import time 

# ----------------------------------------------------------------
# Variables globales
# ----------------------------------------------------------------

#Liste des agents (ID)
agents=[]
#Liste des agents contaminés (ID) 
agents_contamines=[]
#Liste des états d'autonomie des agents (booleen)
sontAutonomes=[]



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
couleur_piece="purple"
nb_pieces=6
tabpieces=[]
RAYON_PIECE=4

#score
score_init=0
score_piece=5

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

#Dimensions
LARG_CANVAS = 760
HAUT_CANVAS = 680

LARG_CASE=40#Largeur
HAUT_CASE=40#Hauteur

#Couleurs Agents    

#creation de différence couleur pour agents autonomes================================================================
COULEUR_AUTO=[]
COULEUR_AUTO.append("orange")
COULEUR_AUTO.append("darkorange")
COULEUR_AUTO.append("navajowhite")
COULEUR_AUTO.append("red")

#====================================================================================================================

#COULEUR_AUTO="orange"
COULEUR_NON_AUTO="yellow"
COULEUR_PROBLEME="red"

#Couleur des agents contaminés 
COULEUR_CONTAMINES = "red"
#Etat des animations et déplacements
etat_actif_depl_anim = False

#Demande d'arrêt
dde_arret = False

niveau1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
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
        if (niveau1[i][j]==1):
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

    

    #boutons de control WASD ==================================================================================================================      
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
    global vitX,vitY,coordXInit,coordYInit,agents,sontAutonomes
    
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
        if not sontAutonomes[i] and i == 0:    # à condition que ce soit le premier agent====================================================
            vitX[i]=pVitesseX
            vitY[i]=pVitesseY

    
    #Couleur des boutons utilisés
    init_couleurs()
    pBtn.config(bg="blue")

    dde_arret = False
    
    if etat_actif_depl_anim == False :
        deplacements()


# Ajouter une deuxième fonction pour controler le 2ème agent avec les touches awsd==============================================================

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
        deplacement(noAgent,sontAutonomes[i],etat_fonc,pNoAgentContamine)
        i+=1
    for noAgentContamine in range(len(noAge))

    if dde_arret == False :#Tant que le jeu ne doit pas être arrêté
        fen_princ.after(100, deplacements)#Patienter 100ms afin d'appeler à nouveau cette même fonction (récursivité)
    else:
        dde_arret = False #Arrêt pris en compte et réinitialisé
        etat_actif_depl_anim = False #Animation désactivée
        

"""
Obj: Gestion des déplacements de tous agents

"""
def deplacement(pNoAgent, pAutonomie, etat_fonc, pNoAgentContamine):
    global agents, vitX, vitY, murs,k
    global etat_actif_depl_anim
    
    #Initialisation
    etat_actif_depl_anim = True
    mod_angle = 0


    #Récupération des coordonnées de l'agent
    coordActuelles = gestionCanvas.coords(agents[pNoAgent])
    # récupération des coordonnées de l'agent contaminé
    coordActuellesContamine = gestionCanvas.coords(agents_contamines[pNoAgentContamine])

    #Liste des éléments présents dans la zone devant le Joueur (anticipation en fonction de la direction de la vitesse)
    liste_obstacles = gestionCanvas.find_overlapping(coordActuelles[0]+vitX[pNoAgent],coordActuelles[1]+vitY[pNoAgent],
                                                     coordActuelles[2]+vitX[pNoAgent],coordActuelles[3]+vitY[pNoAgent])
    #Liste des éléments présents dans la zone devant l'agent contaminé.
    liste_obstacles_agents_contamines = gestionCanvas.find_overlapping(coordActuellesContamine[0]+vitX[pNoAgentContamine],coordActuellesContamine[1]+vitY[pNoAgentContamine],
                                                     coordActuellesContamine[2]+vitX[pNoAgentContamine],coordActuellesContamine[3]+vitY[pNoAgentContamine])
    collisionPiece = False #vrai si le joueur entre en collision avec une pièce
    collisionAutonome = False #Vrai si le joueur s'apprête à entrer en collision avec un agent autonome
    collisionMur = False #Vrai si le joueur s'apprête à entrer en collision avec un mur
    collisionContamineAutonome = False # vrai si un agent autonome entre en collison avec un agent contaminé
    collisionContamineAgent = False # vrai si un agent non autonome entre en collision avec un agent contaminé
    
    if len(liste_obstacles) > 0 :#Détection de l'obstacle

        for obs in liste_obstacles : #Parcours de la liste des entités présentes dans la zone

            if obs != agents[pNoAgent] : #Collision du joueur avec un autre : mur ou agent autonome ou pièces ou agent contaminé ?

                #Vérifier si obs est un mur
                m = 0
                while ( m<len(murs) and collisionMur==False):
                    if obs == murs[m]:
                        collisionMur=True#Collision avec un mur détectée 
                    else:
                        m=m+1
                #vérifier si obs est un agent autonome 
                if (not collisionMur):
                    collisionAutonome = True
                #vérifier si obs est une pièce
                p = 0
                while (m<len(tabpieces) and collisionPiece == False):
                    if obs == tabpieces[p]: #si il y a collision avec une pièce, exécuter les instructions ci-dessous :
                        collisionPiece = True 
                    else:
                        p += 1
                if (not collisionMur) and (not collisionPiece):
                    collisionAutonome = True #Collision avec un agent autonome détectée
                break
    if len(liste_obstacles_agents_contamines) > 0 :#Détection de l'obstacle

        for obs in liste_obstacles_agents_contamines : #Parcours de la liste des entités présentes dans la zone

            if obs != agents_contamines[pNoAgentContamine] : #Collision de l'agent contaminé avec un autre : mur ou agent autonome ou pièces ou agent normal ?

                #Vérifier si obs est un mur
                m = 0
                while ( m<len(murs) and collisionMur==False):
                    if obs == murs[m]:
                        collisionMur=True#Collision avec un mur détectée 
                    else:
                        m=m+1
                #vérifier si obs est un agent autonome normal
                if (not collisionMur): #si ce n'est pas une collision avec un mur, alors c'est une collision avec un agent autonome normal
                    collisionAutonome = True
                #vérifier si obs est une pièce
                p = 0
                while (m<len(tabpieces) and collisionPiece == False):
                    if obs == tabpieces[p]: #si il y a collision avec une pièce, exécuter les instructions ci-dessous :
                        collisionPiece = True 
                    else:
                        p += 1
                if (not collisionMur) and (not collisionPiece):
                    collisionAutonome = True #Collision avec un agent autonome détectée
                break
        
                    
    

    if collisionAutonome == True:#Changement de la couleur de l'agent si il est en collision
        gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_PROBLEME)
        if pNoAgent == 0 or pNoAgent == 1 :                              # vérifier si l'agent en collision est non autonome===================================================================================================
            etat_fonc[pNoAgent] -= 5                                     # diminuer son niveau de vie=========================================================================================================================
            print ("Etat de l'agent",pNoAgent,etat_fonc[pNoAgent])
        if pNoAgent == 5:
            if etat_fonc[0]>0 and etat_fonc[1] > 0:
                time.sleep(8)
                etat_fonc[pNoAgent] -= 1
                print(etat_fonc[pNoAgent])
            
            if collisionContamineAgent == True : #si il y a une collision d'un agent contaminé avec un agent non contaminé non autonome :
                gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_CONTAMINES) #changer la couleur de l'agent non autonome
                contamines.append(agents.pop(pNoAgent)) #l'enlever de la liste des agents non autonomes et le rajouter dans la liste d'agents contaminés
                etat_fonc_contamines.append(100)
                
            if collisionContamineAutonome == True : #si il y a une collision d'un agent contaminé avec un agent non contaminé autonome :
                gestionCanvas.itemconfig(agents[pNoAgent], fill=COULEUR_CONTAMINES) #changer la couleur de l'agent autonome
                contamines.append(agents.pop(pNoAgent)) #l'enlever de la liste des agents non autonomes et le rajouter dans la liste d'agents contaminés
            
            #Inclure les couleurs choisis  pour revenir a la couleur initiale apres collision selon le numero de l'agent autonome [2 3 4 5] vu que les deux premiers sont non autonomes=============================================
    
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
        gestionCanvas.itemconfig(agents[pNoAgent], fill='black')#COULEUR_NON_AUTO)
      
    
    if collisionMur :#Stopper l'agent
        vitX[pNoAgent]=0
        vitY[pNoAgent]=0

    else :  


        # Verifier si l'etat de fonctionement des agents est egale a 0====================================================
        if etat_fonc[pNoAgent] <= 0 :
        
            vitX[pNoAgent]=0  #immobiliser l'agent
            vitY[pNoAgent]=0
            #arret()
            if etat_fonc[pNoAgent] <= 0 :   # si le deuxième agent est immobilisé, arret du jeu
                arret()
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



                #placement de l'agent
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
Obj: Réinitiaisation toutes les positions et les vitesses et arrêt des animations et déplacements
"""
def depart():

    global vitX, vitY
    
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
    global dde_arret
        
    #Mise à jour des boutons
    init_couleurs()
    btnArret.config(bg="blue")

    #Mise à jour de la variable globale utilisée dans les déplacements
    dde_arret = True



# ----------------------------------------------------------------
# Corps du programme
# ----------------------------------------------------------------

#Paramétrage de la fenêtre principale
fen_princ = Tk()
fen_princ.title("PACAGENT L1 SPI")
fen_princ.geometry("900x700")#Dimensions de la fenêtre
fen_princ.bind("<Key>",evenements)#Définition de la fonction de gestion des évènements clavier

#Pramétrage du Canvas
gestionCanvas = Canvas(fen_princ, width=LARG_CANVAS, height=HAUT_CANVAS, bg='ivory', bd=0, highlightthickness=0)
gestionCanvas.grid(row=0,column=0, padx=10,pady=10)

#Affichage des murs du niveau 1
murs=[]
for i in range(len(niveau1)):
    for j in range(len(niveau1[i])):
        if (niveau1[i][j]==0):
            murs.append(gestionCanvas.create_rectangle(i*LARG_CASE, j*HAUT_CASE,(i+1)*LARG_CASE, (j+1)*HAUT_CASE, fill="blue"))

#Affichage des agents gérés par l'utilisateur
nbAgentNonAutonomes=2
for i in range(nbAgentNonAutonomes):
    creationAgent(False)

#Affichage des agents autonomes
nbAgentAutonomes=3
for i in range(nbAgentAutonomes):
    creationAgent(True)
    
#Affichage des agents autonomes contaminés :
nbAgentAutonomesContamines=1
for i in range(nbAgentAutonomesContamines):
    creationAgent(True) 

for i in range(nb_pieces):
    creationPieces()

#Zone dédiée aux boutons
zoneBtn = Frame(fen_princ)
zoneBtn.grid(row=0,column=1,ipadx=5)


#Zone dédiée aux boutons secondaire =======================================================================================================
zoneBtn1 = Frame(fen_princ)
zoneBtn1.grid(row=0,column=2,ipadx=5)
#==========================================================================================================================================


#Boutons directionnels 
btnDroite = Button(zoneBtn, text=">>>", fg="yellow", bg="black", command=lambda: demarrage(VIT_MAX_Autonome,0,btnDroite))
btnDroite.pack(fill=X)

btnGauche = Button(zoneBtn, text="<<<", fg="yellow", bg="black", command=lambda:demarrage(-VIT_MAX_Autonome,0,btnGauche))
btnGauche.pack(fill=X)

btnHaut = Button(zoneBtn, text="^^^", fg="yellow", bg="black", command=lambda:demarrage(0,-VIT_MAX_Autonome,btnHaut))
btnHaut.pack(fill=X)

btnBas = Button(zoneBtn, text="vvv", fg="yellow", bg="black", command=lambda:demarrage(0,VIT_MAX_Autonome,btnBas))
btnBas.pack(fill=X)




#Boutons directionnels secondaires=======================================================================================================
D = Button(zoneBtn1, text="D", fg="yellow", bg="black", command=lambda:demarrage2EME(VIT_MAX_Autonome,0,D))
D.pack(fill=X)

Q = Button(zoneBtn1, text="Q", fg="yellow", bg="black", command=lambda:demarrage2EME(-VIT_MAX_Autonome,0,Q))
Q.pack(fill=X)

Z = Button(zoneBtn1, text="Z", fg="yellow", bg="black", command=lambda:demarrage2EME(0,-VIT_MAX_Autonome,Z))
Z.pack(fill=X)

S = Button(zoneBtn1, text="S", fg="yellow", bg="black", command=lambda:demarrage2EME(0,VIT_MAX_Autonome,S))
S.pack(fill=X)
#=========================================================================================================================================



#Boutons d'arrêt et de réinitialisation
btnArret = Button(zoneBtn, text="STOP", fg="yellow", bg="red", command=arret)
btnArret.pack(fill=X)
btnInit = Button(zoneBtn, text="INIT", fg="yellow", bg="red", command=depart)
btnInit.pack(fill=X)

#Rafraichissement de la fenêtre et de tout son contenu
fen_princ.mainloop()
