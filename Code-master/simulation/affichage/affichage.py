import numpy as np
import time
import random
from tkinter import*

class AffichageTK(object):
    
    #rectangle_robot
    def __init__(self,arene,robot):
        self.robot=robot
        self.arene=arene
        self.dim=arene.taille
        self.l,self.r = None,None
    
    def affiche_obstacle(self):
        for i in self.arene.obstacles:
            self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='yellow')
    

    def start_affichage(self):
        self.root = Tk()                            # root variable contenant la fenÃªtre
        self.root.title('Tuto')                     # Nom de la fenÃªtre    
        
        self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='white')            # crÃ©ation de la fenÃªtre 
        self.can.pack()
        
        quitter = Button(self.root, text = 'quitter', command=self.deleteMe)                # bouton pour quitter la fenÃªtre
        quitter.pack(side=BOTTOM)
        if not self.arene.stop:
            self.root.after(5,self.updateA)

        self.root.mainloop()
        
    def updateA(self):
        self.deleterobot()
        self.affiche_robot()
        self.root.after(5,self.updateA)


    def deleteMe(self):
        self.arene.stop = True
        time.sleep(1)
        self.root.destroy()
    def affiche_robot(self):
        #print(self.robot.x,self.robot.y)
        #self.r = self.can.create_rectangle(self.robot.y, self.robot.x, self.robot.y+self.robot.longueur, self.robot.x+self.robot.largeur, fill="black")
        #self.r=self.can.create_rectangle(self.robot.x-(self.robot.longueur/2), self.robot.y-(self.robot.longueur/2), self.robot.x+(self.robot.longueur/2), self.robot.y+(self.robot.longueur/2), fill="green")
        self.r=self.can.create_polygon(self.robot.a[0],self.robot.a[1],self.robot.b[0],self.robot.b[1],self.robot.c[0],self.robot.c[1],self.robot.d[0],self.robot.d[1],fill="#FF1493")
        self.l=self.can.create_line(self.robot.x, self.robot.y, self.robot.ptv[0] , self.robot.ptv[1], arrow='last', fill='black')
        self.can.create_oval(self.robot.x, self.robot.y, self.robot.x+1, self.robot.y+1, fill="#606060")
        self.can.update()
    def deleterobot(self):
        if self.l:
            self.can.delete(self.l)
        if self.r: 
            self.can.delete(self.r)
        
    """def main(self):
        angle=random.randint(0,180)
        self.robot.rotationDroite(angle)
        while(True):
            time.sleep(0.02)
            self.affiche_robot()
            if (self.arene.collision()):
                self.robot.avance_vers()
            else :
                angle=random.randint(0,180)
                self.robot.rotationDroite(angle)
            self.can.update()
            self.deleterobot()"""