import classe as cl 
import excecute as ex 

Map = ex.initMap(10)
Map = ex.randomMap(Map)
ex.affiche(Map)
def CommencerPartie1èreVersion(): #à modif plus tard pour + 2 joueurs    
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
        pass
        

                        
            
            
