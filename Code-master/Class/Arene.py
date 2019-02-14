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
    
    


    def LectureFichier(self,fichier):
        i=-1
        if  not (fichier[i]=='t' and fichier[i-1]=='x' and fichier[i-2]=='t'):  #lit un fichier .txt pris en parametre et met toute les valeurs du fichier dans la variable Matrice.
            print("Erreur dans le type de fichier")
        else:
            f = open(fichier,'r')
            contenu = f.read()
            x=0
            y=0
            for e in contenu:
                if not(e=='[' or e==']' or e==',' or e==' ', e=='.'):
                    self.Matrice[x][y]=int(e)
                    y+=1
                    if(y==self.taille):
                        x+=1
                        y=0
                    
            f.close()
            
            
            
    def EcritureFichier(self,fichier):                                 #Modifie un fichier .txt pris en parametre et met toute les valeurs de l'arene dedans.
        i=-1
        if  not (fichier[i]=='t' and fichier[i-1]=='x' and fichier[i-2]=='t'):
            print("Erreur dans le type de fichier")
        else:
            f = open(fichier,'w')
            for e in self.Matrice:
                f.write(str(e))
            f.close()
    
    
    
    
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

    def Collision(self, x, y):
        """ Si la position (x, y) est le bord de l'arene ou si un 
        obstacle s'y trouve la fonction renvoie false sinon true"""

        if(x<0 or x>self.taille-1):
            return false
        if(y<0 or y>self.taille-1):
            return false
        else:
            if (self.Matrice[x][y]==1):
                return false
            return true
            
    def Avancer(self,u,v):
        if((u>self.taille ) or (v>self.taille) or (self.taille<0) or (self.taille<0)):
            print("Le point est hors de l'arène")
            return
        #print(self.Matrice)
        print("\n")
        while (self.robot.x != u):
            if (u>self.robot.x):
                self.robot.x=self.robot.x+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x-1][self.robot.y]=0
                #print(self.Matrice)
                #print("\n")
            else :
                self.robot.x=self.robot.x-1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x+1][self.robot.y]=0
                #print(self.Matrice)
                #print("\n")
                
        while (self.robot.y != v):
            if (v>self.robot.y):
                self.robot.y=self.robot.y+1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y-1]=0
                #print(self.Matrice)
                #print("\n")
            else :
                self.robot.y=self.robot.y-1
                self.Matrice[self.robot.x][self.robot.y]=2
                self.Matrice[self.robot.x][self.robot.y+1]=0
                #print(self.Matrice)
#print("\n")

