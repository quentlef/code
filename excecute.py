import random as rd
import tkinter as tk 
import classe as cl

# Exemple d'utilisation de la classe
joueur1 = cl.Unite.Archer("unité1",pv=10)
ennemi1 = cl.Unite.Archer("unité2",pv=5 )

# Attaque du joueur1 sur l'ennemi1
joueur1.attaquer(ennemi1)            
            
            


        
''' 
Principes des cases :
Plaines = Occtroit +2 nourriture à la ville rattaché
Montagne = aucune troupes ne peut passer par cette case, +2 pour université si à côté
Carrière = Occtroit +2 engrenage à la ville rattaché 
'''  
Plaines = cl.Case("Plaines", "Nourriture = + 2" , "rien", "P")
Montagne = cl.Case("Montagne", "rien" , "+1 si université", "M")
Carrière = cl.Case("Carrière", "Production = + 2" , "rien", "C")


def changer_nom(joueur):
    nom = input("Rentrer votre nom d'utilisateur")
    joueur.nom = nom

#Initialisation des variables Villes , Joueur
def CommencerPartie(): #à remplir
    Lille = cl.Ville("Lille")
    Paris = cl.Ville("Paris")
    Gaia = cl.Joueur("Gaia")
    j1 = cl.Joueur("J1")
    j2 = cl.Joueur("J2")
    Lille.joueur = j1
    Paris.joueur = j2
    #choisir un build pour la ville 1:
    for Ville in cl.Ville:
        Build_voulue = input("Production ?")
        if Ville.build == None:
            archer1 = cl.Production(cl.Unite.Archer)
            Ville.build = archer1 = cl.Production(cl.Unite.Archer)




def TourPasse():
    return 

def initialisationJoueur(n):
    Liste_Joueur = []
    for i in range(n):
        nom = ("Joueur {0}".format(i+1))
        Liste_Joueur.append(nom)
       
    return Liste_Joueur

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
            if 0 <= random <0.20 :
                Map[i][j] = 'T'
            elif 0.20<= random < 0.40 :
                Map[i][j] = 'E'
            elif 0.40 <= random < 0.90:
                Map[i][j] = 'H'
            elif 0.90 <= random <= 1:
                Map[i][j] = 'P'
            else:
                print("marche pas")  
    return Map


def AfficheMap(Map):
    for i in range(len(Map)):
        print(Map[i])


def affiche():
    Map = randomMap(initMap(10))
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
            if Map[i][j] == 'H':
                Bgcolour = 'green'    
            elif Map[i][j] == 'E':
                Bgcolour = 'blue'
            elif Map[i][j] == 'P':
                Bgcolour = 'grey'
            elif Map[i][j] == 'T' :
                Bgcolour = "#A5A52A"
            elif Map[i][j] == 'V' :
                Bgcolour = "#A5A52A"
            else:
                Bgcolour = 'red'
                
            m.add(tk.Label(m, text=(Map[i][j]), background=Bgcolour, anchor=tk.CENTER, relief=tk.RAISED, height=5,width=15))
    p.pack()
    
    fenetre.mainloop()
