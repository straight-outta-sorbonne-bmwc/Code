import numpy as np
import random
class Arene:
    def __init__(self,taille):
        self.Matrice=np.zeros((taille,taille))
    
    def ajouterObstacleAleatoire():
        for i in range(15):
            u=random.randint(0,9)
            v=random.randint(0,9)
            self.Matrice[u][v]=1
