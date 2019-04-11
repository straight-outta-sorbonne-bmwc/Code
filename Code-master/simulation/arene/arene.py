#coding: utf-8

import numpy as np
import math
import random
import time

class Arene:
    obstacles = []      # liste d'obstacles
    def __init__(self, robot):
        self.taille=1000        # la taille de l'arene est fixe maintenant comme sa pas de prise de tête
        self.robot=robot
        self.stop = False
        self.lasttime=time.time()
        self.lastd=0
   

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
        for i in range(15):
            u=random.randint(0,self.taille-1)
            v=random.randint(0,self.taille-1)
            self.obstacles.append(Obstacle.Obstacle(u, v))
           

    def add_obstacle(self, x, y):
        if(x<0 or x>self.taille-1):
            print("Erreur sur la valeur de x")
        elif(y<0 or y>self.taille-1):
            print("Erreur sur la valeur de y") 
        else:
            self.obstacles.append(Obstacle.Obstacle(x, y))

    """def collision(self, x, y):
        #Renvoie true si il peut avancer, false sinon. Test juste si le robot est au bord de l'arene, 
        #   x et y correspondent à la nouvelle position du robot
        if(x<0 or y<0 or x>self.taille or y>self.taille):
            return False
        u_robot = self.robot.direction[0]+self.robot.longueur/2
        v_robot = self.robot.direction[1]+self.robot.largeur/2
        milieu = (x+u_robot, y+v_robot)
        a = (milieu[0]+self.rotation(90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(90, self.robot.direction)[1]+self.robot.largeur/2)
        b = (milieu[0]+self.rotation(-90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(-90, self.robot.direction)[1]+self.robot.largeur/2)
        milieu = (x-u_robot, y-v_robot)
        c = (milieu[0]+self.rotation(90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(90, self.robot.direction)[1]+self.robot.largeur/2)
        d = (milieu[0]+self.rotation(-90, self.robot.direction)[0]+self.robot.largeur/2, milieu[1]+self.rotation(-90, self.robot.direction)[1]+self.robot.largeur/2)
        if(a[0]<0 or b[0]<0 or c[0]<0 or d[0]<0 or a[1]<0 or b[1]<0 or c[1]<0 or d[1]<0 or a[0]>self.taille or b[0]>self.taille or c[0]>self.taille or d[0]>self.taille or a[1]>self.taille or b[1]>self.taille or c[1]>self.taille or d[1]>self.taille):
            return False
        else :
            return True"""
        
    def collision(self):
        res=self.robot.avance_vers()
        for i in range(0,4):
            for j in range(0,2):
                if(j==0 and res[i][j]>=self.taille):
                    return False
                if(j==1 and res[i][j]>=self.taille):
                    return False
                if(j==0 and res[i][j]<=0):
                    return False
                if(j==1 and res[i][j]<=0):
                    return False
        return True


    """def rotation(self,angle, v):
        #angle positif = sens des aiguille d'une montre et angle negatif = sens inverse
        vx, vy=v[0], v[1]
        vtemp = 0.0
        vtemp = round(v[0] * math.cos(math.radians(angle)) - vy * math.sin(math.radians(angle)))
        vy = round(- v[0] * math.sin(math.radians(angle)) + vy * math.cos(math.radians(angle)))
        return (vtemp, vy)"""
    
    
    def est_vide(self,x,y):
        for i in range(len(self.obstacles)):
            if ((self.obstacles[i].x==x) and (self.obstacles[i].y==y) or (self.robot.x==x and self.robot.y==y)):
                return False
            else:
                return True

    def update(self):
        # angle=random.randint(0,180)
        # time.sleep(0.02)
        # if (self.collision()):
        #     self.robot.avance_vers()
        # else :
        #     angle=random.randint(0,180)
        #     self.robot.rotationDroite(angle)
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
            
        
            
            
