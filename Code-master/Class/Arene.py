import numpy as np
import random
import Obstacle
class Arene:
    obstacles = []      # liste d'obstacles
    def __init__(self,taille, robot):
        if(type(taille)==int):
            if(taille>0):
                self.taille=taille
                self.robot=robot
            else:
                print("Erreur de taille")
    

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
        """ la méthode ajoute 15 obstacles aléatoirement dans la liste d'obstacle"""
        for i in range(15):
            u=random.randint(0,self.taille-1)
            v=random.randint(0,self.taille-1)
            self.obstacles.append(Obstacle.Obstacle(u, v))
           

    def AddObstacle(self, x, y):
        if(x<0 or x>self.taille-1):
            print("Erreur sur la valeur de x")
            return
        if(y<0 or y>self.taille-1):
            print("Erreur sur la valeur de y")
            return 
        else:
        	self.obstacles.append(Obstacle.Obstacle(x, y))

                
    

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
            
