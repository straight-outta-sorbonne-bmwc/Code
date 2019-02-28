import math
from .robot import Robot
class Direction:
    def __init__(self,u,v):
        self.u=u
        self.v=v
        
    def Rotation(self,angle,robot):#angle positif = sens des aiguille d'une montre et angle negatif = sens inverse
        xM=robot.direction.u-robot.x
        yM=robot.direction.v-robot.y
        self.u= round(xM * math.cos(math.radians(angle)) + yM * math.sin(math.radians(angle)) + robot.x,2)
        self.v = round(- xM * math.sin(math.radians(angle)) + yM * math.cos(math.radians(angle))+ robot.y,2)
        
        
#test=Direction(1.0,0.0)
#print(test.u)
#print(test.v)
#ro=Robot.Robot(0.0,0.0,50.0,50.0,test)
#test.Rotation(90,ro)
#print(test.u)
#print(test.v)
