class AffichageTK(object):

	#rectangle_robot
	def __init__(self, arene, robot):
		self.arene=arene
		self.robot=robot
		self.dim=arene.taille
		self.root = Tk()							# root variable contenant la fenêtre
		self.root.title('Tuto')						# Nom de la fenêtre	
		self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='pink')			# création de la fenêtre 
		self.can.pack()
		self.afficheObstacle()
		self.afficheRobot()												
		quitter = Button(self.root, text = 'quitter', command=self.root.destroy)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)							# emplacement des boutons
		self.root.mainloop()

	def afficheObstacle(self):
	    for i in self.arene.obstacles:
	    	self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='yellow')

		
	def afficheRobot(self):
		self.can.create_rectangle(self.robot.y, self.robot.x, self.robot.y+self.robot.longueur, self.robot.x+self.robot.largeur, fill="black")


# Programme principal
if __name__ == '__main__':
	import numpy as np
	import Arene
	import Robot
	from tkinter import*												
	#test----------------------------
	robot=Robot.Robot(500, 500, 100, 50)
	arene=Arene.Arene(1000, robot)
	arene.ajouterObstacleAleatoire()
	f = AffichageTK(arene, robot)
