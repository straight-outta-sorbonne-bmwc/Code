from . import calcul

class Robot:
    WHEEL_DROIT = 1
    WHEEL_GAUCHE = 2
    def __init__(self,x,y,longueur,largeur):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.ptv=[self.x+(self.longueur/2), self.y]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]#position du vecteur
        self.a=[self.x-(self.longueur/2),self.y+(self.largeur/2)]
        self.b=[self.x+(self.longueur/2),self.y+(self.largeur/2)]
        self.d=[self.x-(self.longueur/2),self.y-(self.largeur/2)]
        self.c=[self.x+(self.longueur/2),self.y-(self.largeur/2)]
        
    def rotationDroite(self,angle):
        #xm=self.direction.u-self.x
        #ym=self.direction.v-self.y
        #self.u= round(xm * math.cos(math.radians(angle)) + ym * math.sin(math.radians(angle)) + self.x,2)
        #self.v = round(- xm * math.sin(math.radians(angle)) + ym * math.cos(math.radians(angle))+ self.y,2)
        rot=calcul.rotatePoint(self.ptv, [self.x,self.y], angle*(-1))
        self.ptv=[rot[0],rot[1]]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]
        self.a=calcul.rotatePoint(self.a, [self.x,self.y], angle*(-1))
        self.b=calcul.rotatePoint(self.b, [self.x,self.y], angle*(-1))
        self.c=calcul.rotatePoint(self.c, [self.x,self.y], angle*(-1))
        self.d=calcul.rotatePoint(self.d, [self.x,self.y], angle*(-1))
    
    def rotationGauche(self,angle):
        rot=calcul.rotatePoint(self.ptv, (self.x,self.y), angle)
        self.ptv=[rot[0],rot[1]]
        c=calcul.calculvecteur([self.x,self.y], self.ptv)
        self.direction=[c[0], c[1]]
        self.a=calcul.rotatePoint(self.a, [self.x,self.y], angle)
        self.b=calcul.rotatePoint(self.b, [self.x,self.y], angle)
        self.c=calcul.rotatePoint(self.c, [self.x,self.y], angle)
        self.d=calcul.rotatePoint(self.d, [self.x,self.y], angle)
    
    def avance_vers(self):
        a=[self.x, self.y]
        ptvbis=self.ptv
        vect=calcul.calculvecteur(a, ptvbis)
        vnor=calcul.normalize(vect)
        self.x=a[0]+vnor[0]
        self.y=a[1]+vnor[1]
        self.ptv[0]=ptvbis[0]+vnor[0]
        self.ptv[1]=ptvbis[1]+vnor[1]
        self.a[0]=self.a[0]+vnor[0]
        self.a[1]=self.a[1]+vnor[1]
        self.b[0]=self.b[0]+vnor[0]
        self.b[1]=self.b[1]+vnor[1]
        self.c[0]=self.c[0]+vnor[0]
        self.c[1]=self.c[1]+vnor[1]
        self.d[0]=self.d[0]+vnor[0]
        self.d[1]=self.d[1]+vnor[1]
        l=[self.a,self.b,self.c,self.a]
        return l
