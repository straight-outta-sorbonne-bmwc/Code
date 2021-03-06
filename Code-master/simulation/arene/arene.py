#coding: utf-8

import numpy as np
import math
import random
import time
from . import obstacle

class Arene:
    obstacles = []      # liste d'obstacles
    def __init__(self, robot):
        self.taille=1000        # la taille de l'arene est fixe maintenant comme sa pas de prise de tête
        self.robot=robot
        self.stop = False
        self.lasttime=time.time()
        self.lastd=0
        self.robot.arene=self
   

    def lecture_fichier(self,fichier):
        if  not (fichier[-1]=='l' and fichier[-2]=='k' and fichier[-3]=='p'):
            print("Erreur dans le type de fichier")
            return
        with open(fichier,'rb') as f:
            new_arene=pickle.load(f)
        return new_arene

            
            
    def ecriture_fichier(self,fichier):                                 #Modifie un fichier .txt pris en parametre et met toute les valeurs de l'arene dedans.
        if  not (fichier[-1]=='l' and fichier[-2]=='k' and fichier[-3]=='p'):
            print("Erreur dans le type de fichier")
        else:
            with open(fichier,'wb') as f:
                pickle.dump(self,f)
    
    def ajouter_obstacle_aleatoire(self):
        """ la méthode ajoute 15 obstacles aléatoirement dans la liste d'obstacle"""
        for i in range(5):
            u=random.randint(0,self.taille-1)
            v=random.randint(0,self.taille-1)
            self.obstacles.append(obstacle.Obstacle(u, v))
           

    def add_obstacle(self, x, y): #ajoute un obstacle à la position x,y
        if(x<0 or x>self.taille-1):
            print("Erreur sur la valeur de x")
        elif(y<0 or y>self.taille-1):
            print("Erreur sur la valeur de y") 
        else:
            self.obstacles.append(obstacle.Obstacle(x, y))


        
    
    def get_distance(self):#return la distance du robot à l'obstacle 
                                                                                                                                                                
        for i in range (5, 8000):
            for j in self.obstacles:
                a=[self.robot.a[0]+self.robot.dir[0]*(-i) , self.robot.a[1]+self.robot.dir[1]*(-i) ]
                b=[self.robot.b[0]+self.robot.dir[0]*i ,self.robot.b[1]+self.robot.dir[1]*i ]
                c=[self.robot.c[0]+self.robot.dir[0]*i , self.robot.c[1]+self.robot.dir[1]*i ]
                d=[self.robot.d[0]+self.robot.dir[0]*(-i), self.robot.d[1]+self.robot.dir[1]*(-i)]

                if ((abs(a[0]- j.x)<= j.taille/2) and ( abs(a[1]-j.y)<= j.taille/2 )) or ((a[0] >= self.taille) or (a[1] >= self.taille)) or ((a[0] <= 0) or (a[1] <= 0)): 
                
                    return i
                if ((abs(b[0]- j.x)<= j.taille/2) and ( abs(b[1]-j.y)<= j.taille/2 )) or ((b[0] >= self.taille) or (b[1] >= self.taille)) or ((b[0] <= 0) or (a[1] <= 0)): 
                  
                    return i
                if ((abs(c[0]- j.x)<= j.taille/2) and ( abs(c[1]-j.y)<= j.taille/2 )) or ((c[0] >= self.taille) or (c[1] >= self.taille)) or ((c[0] <= 0) or (a[1] <= 0)): 
                
                    return i
                if ((abs(d[0]- j.x)<= j.taille/2) and ( abs(d[1]-j.y)<= j.taille/2 )) or ((d[0] >= self.taille) or (d[1] >= self.taille)) or ((d[0] <= 0) or (a[1] <= 0)): 
                    
                    return i
        return 8190

    def update(self): #update pour le monde simulé permettant de mettre à jour la position du robot dans l'aréne

        dt=time.time()-self.lasttime
        
        if self.robot.motor_dps_droit==self.robot.motor_dps_gauche :
            distance=(self.robot.motor_pos_gauche*(self.robot.WHEEL_CIRCUMFERENCE)/360)-self.lastd
            
            self.robot.x=self.robot.x+self.robot.dir[0]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))
            self.robot.y=self.robot.y+self.robot.dir[1]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))
            self.robot.ptv=[(self.robot.b[0]+self.robot.c[0])/2, (self.robot.b[1]+self.robot.c[1])/2]

            self.robot.a=[self.robot.a[0]+self.robot.dir[0]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360)), self.robot.a[1]+self.robot.dir[1]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))]
            self.robot.b=[self.robot.b[0]+self.robot.dir[0]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360)), self.robot.b[1]+self.robot.dir[1]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))]
            self.robot.c=[self.robot.c[0]+self.robot.dir[0]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360)), self.robot.c[1]+self.robot.dir[1]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))]
            self.robot.d=[self.robot.d[0]+self.robot.dir[0]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360)), self.robot.d[1]+self.robot.dir[1]*(dt*self.robot.motor_dps_gauche*((self.robot.WHEEL_DIAMETER*math.pi)/360))]   
                 


            self.robot.motor_pos_droit+=dt*self.robot.motor_dps_droit
            self.robot.motor_pos_gauche+=dt*self.robot.motor_dps_gauche            


        
        if self.robot.motor_dps_droit==0 and self.robot.motor_dps_gauche>0:
            distance=(self.robot.motor_pos_gauche*(self.robot.WHEEL_CIRCUMFERENCE)/360)-self.lastd
            angle=distance/((self.robot.WHEEL_BASE_WIDTH*2*math.pi)/360)
            self.robot.rotationDroite(angle) 
            self.robot.motor_pos_gauche+=dt*self.robot.motor_dps_gauche
        

        if self.robot.motor_dps_droit>0 and self.robot.motor_dps_gauche==0:
            distance=(self.robot.motor_pos_droit*(self.robot.WHEEL_CIRCUMFERENCE)/360)-self.lastd
            angle=distance/((self.robot.WHEEL_BASE_WIDTH*2*math.pi)/360)
            self.robot.rotationGauche(angle) 
            self.robot.motor_pos_droit+=dt*self.robot.motor_dps_droit
        
    
        self.lastd+=distance
        self.lasttime=time.time()
            
        
            
            
