#Classe Joueur
class Coordonnees:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Joueur:
    def __init__(self, nom, gold = 0):
        self.nom = nom
        self.gold = gold

class Ville:
    list_villes = []
    population = 1
    production = 1
    orgen = 1
    sciencegen = 1
    def __init__(self, nom, joueur, coord):
        self.nom = nom
        self.joueur = joueur
        self.coord = coord
        self.build = None
        Ville.list_villes.append(self)

class Production:
    def __init__(self, nom):
        self.nom = nom
        self.cout = nom.coutprod
       
            
class territoire:
    def __init__(self,joueur):
        self.joueur = joueur
        self.case_occupé = [] #liste de coords (x,y)
        
class Recherche:
    def __init__(self,nom_recherche,point_recherche_requis):
        self.nom_recherche = nom_recherche
        self.point_recherche_requis = point_recherche_requis   

class Unite:  
    list_Unite = []
    def attaquer(self, cible):
    #regarde la portée
        if self.portee >= 2:
        
            cible.pv -= self.degats
        
            if cible.pv < 0:
                print(f"Attaque réussie ! l'{cible.nom} est morte ")
                del cible
            else :
                print(f"Attaque réussie ! Points de vie restants de la cible : {cible.pv}")
            
        else:
            print("La cible est hors de portée !")      
    class Archer:
        # Attributs de classe partagés
        
        degats = 10
        portee = 2
        coutprod = 5
        pm = 2
        pv = 30
        xp = 0
        attaque = 1
        valeur = 20

        def __init__(self,joueur,nom,coord =(1,1)):
            # Attributs d'instance propres à chaque instance
            self.nom = nom     
            self.coord = coord
            self.joueur = joueur
            Unite.list_Unite.append(self)
            
    class Eclaireur: 
        # Attributs de classe partagés
        
        degats = 5
        portee = 1
        coutprod = 5
        pm = 4
        pv = 30
        xp = 0
        attaque = 1
        valeur = 20
        def __init__(self,joueur,nom,coord =(1,1)):
            # Attributs d'instance propres à chaque instance
            self.nom = nom     
            self.coord = coord
            self.joueur = joueur
            Unite.list_Unite.append(self)
            
    class Guerrier: 
        # Attributs de classe partagés
        
        degats = 10
        portee = 1
        coutprod = 5
        pm = 2
        pv = 50
        xp = 0
        attaque = 1
        valeur = 30
        def __init__(self,joueur, nom,coord =(1,1)):
            # Attributs d'instance propres à chaque instance
            self.nom = nom     
            self.coord = coord
            self.joueur = joueur
            Unite.list_Unite.append(self)



                    
#Initialisation des cases 
class Case:
    def __init__(self, nom, occtroit:[] , bonusprox , caractéristique, etatdeplacement):
        self.nom = nom
        self.occtroit = [0,0,0,0] #[prod,nourriture,science,or]
        self.bonusprox = bonusprox
        self.caractéristique = caractéristique
        self.appartenance = 0
        self.coutPM = etatdeplacement
        
class Case_plateau:
    list_cases = []
    def __init__(self,typecase,coord):
        self.typecase = typecase
        self.coord = coord
        Case_plateau.list_cases.append(self)
        
j1 = Joueur("J1")
j2 = Joueur("J2")
            
class ValeurUnite:
    def __init__(self):
        self.NbrUniteJ1 = 0
        self.ValeurUniteJ1 = 0
        self.NbrUniteJ2 = 0
        self.ValeurUniteJ2 = 0
    def ChangeValeur(self,unite):
        if unite.joueur == j1:
            self.NbrUniteJ1 += 1
            self.ValeurUniteJ1 += unite.valeur
        if unite.joueur == j2:
            self.NbrUniteJ2 += 1
            self.ValeurUniteJ2 += unite.valeur
