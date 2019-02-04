import numpy as np
import random
class Arene:
    def __init__(self,taille):
        if(type(taille)==int):
            if(taille>0 and taille<=50):    
                self.taille=taille
                self.Matrice=np.zeros((self.taille,self.taille))
        else:
            if(taille>50):
                print("Taille > 50")
                self.taille=10
                self.Matrice=np.zeros((self.taille,self.taille))
            else:
                print("Erreur de taille")
                self.taille=10
                self.Matrice=np.zeros((self.taille,self.taille))
                
    def ajouterObstacleAleatoire(self):
        for i in range(15):
            u=random.randint(0,self.taille-1)
            v=random.randint(0,self.taille-1)
            self.Matrice[u][v]=1

    def avancerXPas(self, Pas):
        for i in range (Pas):
            if (self.robot.y+1<self.taille):
                self.robot.y=self.robot.y+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y-1]=0
