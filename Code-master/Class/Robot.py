import math
class Robot:
import calcul

class Robot:
    def __init__(self,x,y,longueur,largeur):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.direction=(1.0,0.0)#(tuple(u,v))
        #Coordonne=[(self.x,self.y),(self.x+self.longueur,self.y),(self.x+longueur,self.y+largeur),(self.x,self.y+self.largeur)] coordonnées de A,B,C,D
    
    def rotation(self,angle):#angle positif = sens des aiguille d'une montre et angle negatif = sens inverse
        xm=self.direction.u-self.x
        ym=self.direction.v-self.y
        self.u= round(xm * math.cos(math.radians(angle)) + ym * math.sin(math.radians(angle)) + self.x,2)
        self.v = round(- xm * math.sin(math.radians(angle)) + ym * math.cos(math.radians(angle))+ self.y,2)
          
    #cette fonction fait avancer le robot pas à pas vers b
    def avancevers(self, b): #prend en paramètre les coordonnées de là où il veut aller sous la forme (x, y)
        a=(self.x, self.y) 
        vect=calcul.calculvecteur(a, b)
        vnor=calcul.normalize(vect)
        self.x=a[0]+vnor[0]
        self.y=a[1]+vnor[1]
        return vnor #retourne le vecteur de deplacement normalisé
            
