#Classe Joeur          
class Joueur:
    def __init__(self, nom, gold = 0):
        self.nom = nom
        self.gold = gold

class Ville:
    def __init__(self, nom):
        self.nom = nom
        self.population = 1
        self.production = 1
        self.orgen = 1
        self.sciencegen = 1

class territoire:
    def __init__(self,joueur):
        self.joueur = joueur
        self.case_occupé = [] #liste de coords (x,y)
        
class Recherche:
    def __init__(self,nom_recherche,point_recherche_requis):
        self.nom_recherche = nom_recherche
        self.point_recherche_requis = point_recherche_requis   
class Unite:
    
    class Archer:
        # Attributs de classe partagés
        degats = 10
        portee = 2

        def __init__(self, nom,xp = 0, pv = 50):
            # Attributs d'instance propres à chaque instance
            self.points_de_vie = pv
            self.nom = nom
            self.experience = xp     
        def attaquer(self, cible):
        #regarde la portée
            if self.portee >= 2:
            
                cible.points_de_vie -= self.degats
            
                if cible.points_de_vie < 0:
                    print(f"Attaque réussie ! l'{cible.nom} est morte ")
                    del cible
                else :
                    print(f"Attaque réussie ! Points de vie restants de la cible : {cible.points_de_vie}")
                
            else:
                print("La cible est hors de portée !")        

                     
#Initialisation des cases 
class Case:
    def __init__(self, nom, occtroit , bonusprox , caractéristique):
        self.nom = nom
        self.occtroit = occtroit
        self.bonusprox = bonusprox
        self.caractéristique = caractéristique
