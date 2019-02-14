import math
class Robot:
    def __init__(self,x,y,longueur,largeur,direction):
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
            
