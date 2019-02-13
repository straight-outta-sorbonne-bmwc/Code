

class AffichageTK(object):
	echelle=25				# à l'échelle x25 sur la fenêtre tkinter	
	tabx=[]
	taby=[]
	k=0
	#rectangle_robot
	def __init__(self, arene, robot):
		self.arene=arene
		self.robot=robot
		self.dim=arene.taille*self.echelle
		self.root = Tk()							# root variable contenant la fenêtre
		self.root.title('Tuto')						# Nom de la fenêtre	
		self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='pink')			# création de la fenêtre 
		self.can.pack()							
		self.coordObstacle(self.arene)
		self.afficheRobot(self.robot)
		obstacle = Button(self.root, text = 'obstacle', command=self.afficheObstacle)
		avance = Button(self.root, text = 'avance', command=self.avancerRobot)																
		quitter = Button(self.root, text = 'quitter', command=self.root.destroy)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)							# emplacement des boutons
		avance.pack(side=RIGHT)
		obstacle.pack(side=LEFT)
		self.root.mainloop()

	def coordObstacle(self, arene): #On récupére les coordonnées des obstacle
	    for i in range(arene.taille):
	        for j in range(arene.taille):
	            if(arene.Matrice[i][j]==1):
	                self.tabx.append(j)
	                self.taby.append(i)
    

	def afficheObstacle(self):
	    if(self.k<len(self.tabx) and self.k<len(self.taby)):
	    	self.can.create_rectangle(self.tabx[self.k]*self.echelle,self.taby[self.k]*self.echelle,self.tabx[self.k]*self.echelle+self.echelle,self.taby[self.k]*self.echelle+self.echelle,fill='yellow')
	    	self.k=self.k+1 
		
	def afficheRobot(self, robot):
		self.rectangle_robot = self.can.create_rectangle(self.robot.y*self.echelle, self.robot.x*self.echelle, self.robot.y*self.echelle+self.robot.taille, self.robot.x*self.echelle+self.robot.taille/2, fill="black")

	def avancerRobot(self):
		if(self.robot.y!=(self.arene.taille-1)):
			print(self.robot.y)
			self.arene.avancerXPas(1)
			self.can.move(self.rectangle_robot, 1*self.echelle, 0)

# Programme principal
if __name__ == '__main__':
	import numpy as np
	import Arene
	import Robot
	from tkinter import*												
	#test----------------------------
	robot=Robot.Robot(5, 5)
	arene=Arene.Arene(10, robot)
	arene.ajouterObstacleAleatoire()
	f = AffichageTK(arene, robot)

#---------------------------------
