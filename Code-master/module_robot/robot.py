import math
import calcul
class Robot:
    def __init__(self,x,y,longueur,largeur):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.direction=(1.0,0.0)#(tuple(u,v))
        #Coordonne=[(self.x,self.y),(self.x+self.longueur,self.y),(self.x+longueur,self.y+largeur),(self.x,self.y+self.largeur)] coordonnées de A,B,C,D
    
    def rotation(self,vecteur):#modifie la direction du robot (vecteur entre -1<=x<=1)
        self.direction[0]=vecteur[0]
        self.direction[1]=vecteur[1]
        
    #cette fonction fait avancer le robot pas à pas vers b
    def avance_vers(self, b): #prend en paramètre les coordonnées de là où il veut aller sous la forme (x, y)
        a=(self.x, self.y) 
        vect=calcul.calcul_vecteur(a, b)
        vnor=calcul.normalize(vect)
        self.x=a[0]+vnor[0]
        self.y=a[1]+vnor[1]
	return vnor #retourne le vecteur de deplacement normalisé
