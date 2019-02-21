import numpy as np
import math
import random
import Obstacle

class Arene:
    obstacles = []      # liste d'obstacles
    def __init__(self,taille, robot):
        self.taille=taille
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

    def Collision(self, x, y):
        """ Renvoie true si il peut avancer, false sinon. Test juste si le robot est au bord de l'arene, 
            x et y correspondent à la nouvelle position du robot"""
        u_robot = self.robot.direction[0]+self.robot.longueur/2
        v_robot = self.robot.direction[1]+self.robot.largeur/2
        milieu = (x+u_robot, y+v_robot)
        a = (milieu[0]+self.rotation(90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(90, self.robot.direction)[1]+self.robot.largeur/2)
        b = (milieu[0]+self.rotation(-90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(-90, self.robot.direction)[1]+self.robot.largeur/2)
        milieu = (x-u_robot, y-v_robot)
        c = (milieu[0]+self.rotation(90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(90, self.robot.direction)[1]+self.robot.largeur/2)
        d = (milieu[0]+self.rotation(-90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(-90, self.robot.direction)[1]+self.robot.largeur/2)
        print(a, b, c, d)
        if(a[0]<0 or b[0]<0 or c[0]<0 or d[0]<0 or a[1]<0 or b[1]<0 or c[1]<0 or d[1]<0 or a[0]>self.taille or b[0]>self.taille or c[0]>self.taille or d[0]>self.taille or a[1]>self.taille or b[1]>self.taille or c[1]>self.taille or d[1]>self.taille):
            return False
        else :
            return True

    def rotation(self,angle, v):
        """angle positif = sens des aiguille d'une montre et angle negatif = sens inverse"""
        vx, vy=v[0], v[1]
        vtemp = 0.0
        vtemp = round(v[0] * math.cos(math.radians(angle)) - vy * math.sin(math.radians(angle)))
        vy = round(- v[0] * math.sin(math.radians(angle)) + vy * math.cos(math.radians(angle)))
        return (vtemp, vy)
