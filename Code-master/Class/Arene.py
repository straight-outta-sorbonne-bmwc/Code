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
            contenu = f.read()#contenu du fichier txt
            res1=0
            res2=0
            x=0
            for e in contenu:
                if x==2:
                    self.obstacles.append(Obstacle.Obstacle(res1,res2))
                    res1=0
                    res2=0
                    x=0
                elif not(e=='[' or e==']' or e==',' or e==' ' or e=='.' or e=='(' or e== ')'):
                    if x==0 :
                        res1=int(e)
                    else:
                        res2=int(e)
                    x+=1
            f.close()
            
            
            
    def EcritureFichier(self,fichier):                                 #Modifie un fichier .txt pris en parametre et met toute les valeurs de l'arene dedans.
        i=-1
        if  not (fichier[i]=='t' and fichier[i-1]=='x' and fichier[i-2]=='t'):
            print("Erreur dans le type de fichier")
        else:
            f = open(fichier,'w')
            for e in self.obstacles:
                f.write(str((e.x,e.y)))
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
        elif(y<0 or y>self.taille-1):
            print("Erreur sur la valeur de y") 
        else:
        	self.obstacles.append(Obstacle.Obstacle(x, y))
