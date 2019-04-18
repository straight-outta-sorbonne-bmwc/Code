from . import calcul
import math
import time


class Robot:
    WHEEL_DROIT = 1
    WHEEL_GAUCHE = 2

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)
    
    def __init__(self,x,y,longueur,largeur):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.dt=time.time()
        self.MOTOR_LEFT= 1
        self.MOTOR_RIGHT = 2
        self.motor_dps_droit=0
        self.motor_dps_gauche=0
        self.motor_pos_droit=0
        self.motor_pos_gauche=0
        self.offset_gauche=0
        self.offset_droit=0
        self.rotate_choix=0
        self.a=[self.x-(self.longueur/2),self.y+(self.largeur/2)]
        self.b=[self.x+(self.longueur/2),self.y+(self.largeur/2)]
        self.c=[self.x+(self.longueur/2),self.y-(self.largeur/2)]
        self.d=[self.x-(self.longueur/2),self.y-(self.largeur/2)]
        self.ptv=[(self.b[0]+self.c[0])/2, (self.b[1]+self.c[1])/2]
        self.dir=calcul.normalize([self.ptv[0]-self.x, self.ptv[1]-self.y])
        self.arene=None
    '''
    @property
    def a(self):
        v=calcul.calculvecteur([self.x,self.y], self.ptv)
        #return [self.x-(self.longueur/2),self.y+(self.largeur/2)]
        return rotatePoint([self.x-(self.longueur/2),self.y+(self.largeur/2)], (self.x, self.y), angle2vect(self.ddepart, v))
    @property
    def b(self): #roue droite
        #return [self.x+(self.longueur/2),self.y+(self.largeur/2)]
        return rotatePoint([self.x+(self.longueur/2),self.y+(self.largeur/2)], (self.x, self.y), angle2vect(self.ddepart, v))
    @property
    def c(self): #roue gauche
        #return [self.x+(self.longueur/2),self.y-(self.largeur/2)]
        return rotatePoint([self.x+(self.longueur/2),self.y-(self.largeur/2)], (self.x, self.y), angle2vect(self.ddepart, v))
    @property
    def d(self):
        #return [self.x-(self.longueur/2),self.y-(self.largeur/2)]
        return rotatePoint([self.x-(self.longueur/2),self.y-(self.largeur/2)], (self.x, self.y), angle2vect(self.ddepart, v))
    '''
    def rotationDroite(self,angle):
        x,y = calcul.rotatePoint((self.x,self.y), self.b, angle*(-1))
        self.x=x
        self.y=y
        self.a=calcul.rotatePoint(self.a, self.b, angle*(-1))
        self.c=calcul.rotatePoint(self.c, self.b, angle*(-1))
        self.d=calcul.rotatePoint(self.d, self.b, angle*(-1))
        self.ptv=[(self.b[0]+self.c[0])/2, (self.b[1]+self.c[1])/2]
        self.dir=calcul.normalize([self.ptv[0]-self.x, self.ptv[1]-self.y])

    def rotationGauche(self,angle):
        self.x=x
        self.y=y
        self.a=calcul.rotatePoint(self.a, self.c, angle*(1))
        self.b=calcul.rotatePoint(self.b, self.c, angle*(1))
        self.d=calcul.rotatePoint(self.d, self.c, angle*(1))
        self.ptv=[(self.b[0]+self.c[0])/2, (self.b[1]+self.c[1])/2]
        self.dir=calcul.normalize([self.ptv[0]-self.x, self.ptv[1]-self.y])

        
 
    def set_motor_dps(self, port, dps):
        if (port==self.MOTOR_LEFT):
            self.motor_dps_gauche=dps
        elif (port==self.MOTOR_RIGHT):
            self.motor_dps_droit=dps
        elif (port == self.MOTOR_RIGHT + self.MOTOR_LEFT):
            self.motor_dps_droit=dps
            self.motor_dps_gauche=dps

    
    def get_motor_position(self):
        return [self.motor_pos_gauche, self.motor_pos_droit]


    def offset_motor_encoder(self, port, offset):
        if port==self.MOTOR_LEFT:
            self.offset_gauche+=offset 
            self.motor_pos_gauche=0
        if port==self.MOTOR_RIGHT:
            self.offset_droit+=offset
            self.motor_pos_droit=0
        if port==self.MOTOR_RIGHT+self.MOTOR_LEFT:
            self.offset_droit+=offset
            self.offset_gauche+=offset
            self.motor_pos_droit=0
            self.motor_pos_gauche=0
            
    def get_distance(self):
        return self.arene.get_distance()


