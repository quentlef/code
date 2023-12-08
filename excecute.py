import random as rd
import tkinter as tk 
import classe as cl


# Attaque du joueur1 sur l'ennemi1
#joueur1.attaquer(ennemi1)            
            
''' 
Principes des cases :
Plaines = Occtroit +2 nourriture à la ville rattaché
Montagne = aucune troupes ne peut passer par cette case, +2 pour université si à côté
Carrière = Occtroit +2 engrenage à la ville rattaché 
'''  
Plaines = cl.Case("Plaines", [0,2,0,0] , "rien", "P", 1)
Montagne = cl.Case("Montagne", [1,0,0,0] , "+1 si université", "M", 10)
Carrière = cl.Case("Carrière", [2,0,0,0] , "rien", "C", 1)


def changer_nom(joueur):
    nom = input("Rentrer votre nom d'utilisateur")
    joueur.nom = nom

def initMap(n):
    L = []
    for i in range(n):
        L.append(n*["Vide"])
    return L

def randomMap(Map):
    n = len(Map)
    for i in range(n):
        for j in range(n):
            random = rd.random()
            if 0 <= random < 0.50 :
                Map[i][j] = "P {}".format((i,j))
                case = cl.Case_plateau(Plaines, (i,j))
                
            elif 0.50<= random < 0.60 :
                Map[i][j] = "M"
                case = cl.Case_plateau(Montagne, (i,j))
                
            elif 0.60 <= random <= 1:
                Map[i][j] = "C"
                case = cl.Case_plateau(Carrière, (i,j))
                
            else:
                print("marche pas")  
    return Map
'''
affiche selon les coordonnés (colonne,ligne)
'''
def affiche(Map):

    print(Map)
    fenetre = tk.Tk()
    Bgcolour = ""
    p = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
    p.pack(side=tk.TOP, expand=tk.Y, fill=tk.BOTH, pady=0, padx=0)
    n = len(Map)
    for i in range(n):
        m = tk.PanedWindow(p, orient=tk.VERTICAL)
        p.add(m)
        for j in range(n):
            if 'P' in (" " + Map[i][j] + " "): 
                Bgcolour = 'green'    
            elif 'M' == Map[i][j]:
                Bgcolour = 'grey'
            elif 'C' == Map[i][j] :
                Bgcolour = 'orange'
            elif 'VJ1' in Map[i][j] :
                Bgcolour = 'blue'
            elif 'VJ2' in Map[i][j] :
                Bgcolour = 'red'
            else :
                Bgcolour = 'white'
                
            m.add(tk.Label(m, text=(Map[i][j]), background=Bgcolour, anchor=tk.CENTER, relief=tk.RAISED, height=5,width=15))
    p.add(tk.Button(p, text="Quit", command=fenetre.destroy))
    p.pack()
    
    fenetre.mainloop()

#Initialisation des variables Villes , Joueur
def CommencerPartie(Map): #à modif plus tard pour + 2 joueurs    
    Gaia = cl.Joueur("Gaia")
    j1 = cl.Joueur("J1")
    j2 = cl.Joueur("J2")
    Lille = cl.Ville("Lille",j1,(0,5))
    Map[0][5] = "VJ1 {}".format(Lille.nom)
    Paris = cl.Ville("Paris",j2,(9,6))
    Map[9][6] = "VJ2 {}".format(Paris.nom)

    Lille.joueur = j1
    Paris.joueur = j2
    #choisir un build pour la ville 1:
    for ville in cl.Ville.list_villes:
        if ville.build == None:
            #Build_voulue = input("Production ?")        
            archer1 = cl.Production(cl.Unite.Archer)
            ville.build = archer1 = cl.Production(cl.Unite.Archer)
                   
def bouge(unite,direction):
    x,y = unite.coord 

    #appel la fonction bouge corresp
    if direction == "haut":
        if y-1>=0:

            for case in cl.Case_plateau.list_cases:
                if (x,y-1) == case.coord:
                    coutdeplace = case.typecase.coutPM
            if unite.pm < coutdeplace :
                return "déplacement impossible"
            else:
                unite.coord = (x,y-1)
        else:
            return "déplacement impossible"
        
    if direction == "bas":
        if y+1<=9:
            for case in cl.Case_plateau.list_cases:
                if (x,y+1) == case.coord:
                   coutdeplace = case.typecase.coutPM
            if unite.pm < coutdeplace :
                return "déplacement impossible"
            else:
                unite.coord = (x,y+1)
        else:
            return "déplacement impossible"
    if direction == "droite":
        if x+1<=9:
            for case in cl.Case_plateau.list_cases:
                if (x+1,y) == case.coord:
                   coutdeplace = case.typecase.coutPM
            if unite.pm < coutdeplace :
                return "déplacement impossible"
            else:
                unite.coord = (x+1,y)
        else:
            return "déplacement impossible"
    if direction == "gauche":
        if x-1>=0:
            for case in cl.Case_plateau.list_cases:
                if (x-1,y) == case.coord:
                   coutdeplace = case.typecase.coutPM
            if unite.pm < coutdeplace : #check cout en déplacement
                return "déplacement impossible"
            else:
                unite.coord = (x-1,y)
        else:
            return "déplacement impossible"

            
        
     
    
def TourPasse():
    return 

def initialisationJoueur(n):
    Liste_Joueur = []
    for i in range(n):
        nom = ("Joueur {0}".format(i+1))
        Liste_Joueur.append(nom)
       
    return Liste_Joueur

def AfficheMap(Map):
    for i in range(len(Map)):
        print(Map[i])


