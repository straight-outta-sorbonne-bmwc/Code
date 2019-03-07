from . import calcul

class Robot:
    def __init__(self,x,y,longueur,largeur):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.ptv=[self.x+(self.longueur/2), self.y]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]
        
    def rotationDroite(self,angle):
        #xm=self.direction.u-self.x
        #ym=self.direction.v-self.y
        #self.u= round(xm * math.cos(math.radians(angle)) + ym * math.sin(math.radians(angle)) + self.x,2)
        #self.v = round(- xm * math.sin(math.radians(angle)) + ym * math.cos(math.radians(angle))+ self.y,2)
        rot=calcul.rotatePoint(self.ptv, [self.x,self.y], angle*(-1))
        self.ptv=[rot[0],rot[1]]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]
    
    def rotationGauche(self,angle):
        rot=calcul.rotatePoint(self.ptv, (self.x,self.y), angle)
        self.ptv=[rot[0],rot[1]]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]
    
    def avance_vers(self):
        a=[self.x, self.y]
        ptvbis=self.ptv
        vect=calcul.calculvecteur(a, ptvbis)
        vnor=calcul.normalize(vect)
        self.x=a[0]+vnor[0]
        self.y=a[1]+vnor[1]
        self.ptv[0]=ptvbis[0]+vnor[0]
        self.ptv[1]=ptvbis[1]+vnor[1]