import numpy as np
import random
class Arene:
    def __init__(self,taille, robot):
        if(type(taille)==int):
            if(taille>0 and taille<=50):    
                self.taille=taille
                self.robot=robot
                self.Matrice=np.zeros((self.taille,self.taille))
                self.Matrice[self.robot.x][self.robot.y]=2
        else:
            if(taille>50):
                print("Taille > 50")
                self.taille=10
                self.robot=robot
                self.Matrice=np.zeros((self.taille,self.taille))
                self.Matrice[self.robot.x][self.robot.y]=2
            else:
                print("Erreur de taille")
                self.taille=10
                self.robot=robot
                self.Matrice=np.zeros((self.taille,self.taille))
                self.Matrice[self.robot.x][self.robot.y]=2
                
    def ajouterObstacleAleatoire(self):
        for i in range(15):
            u=random.randint(0,self.taille-1)
            v=random.randint(0,self.taille-1)
            self.Matrice[u][v]=1

    def avancerXPas(self, Pas):
        for i in range(Pas):
            if (self.robot.y+1<self.taille):
                self.robot.y=self.robot.y+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y-1]=0

                
    def AddObstacle(self, x, y):
        if(x<0 or x>self.taille-1):
            print("Erreur sur la valeur de x")
            return
        if(y<0 or y>self.taille-1):
            print("Erreur sur la valeur de y")
            return 
        else:
        	self.Matrice[x][y]=1
            
            
       def Avancer(self,u,v):
        if((u>self.taille ) or (v>self.taille) or (u<0) or (v<0)):
            print("Le point est hors de l'arène")
            return
        while (self.robot.x != u):
            if (u>self.robot.x):
                self.robot.x=self.robot.x+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x-1][self.robot.y]=0
                
            else :
                self.robot.x=self.robot.x-1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x+1][self.robot.y]=0
                
                
        while (self.robot.y != v):
            if (v>self.robot.y):
                self.robot.y=self.robot.y+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y-1]=0
               
            else :
                self.robot.y=self.robot.y-1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y+1]=0
               
