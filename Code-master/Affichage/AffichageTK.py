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
		self.demo()											
		quitter = Button(self.root, text = 'quitter', command=self.root.destroy)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)							# emplacement des boutons
		self.root.mainloop()

	def afficheObstacle(self):
	    for i in self.arene.obstacles:
	    	self.can.create_rectangle(i.x, i.y, i.x+i.taille, i.y+i.taille,fill='yellow')

		
	def afficheRobot(self):
		self.r = self.can.create_rectangle(self.robot.y, self.robot.x, self.robot.y+self.robot.longueur, self.robot.x+self.robot.largeur, fill="black")


	def vers(self, coord):
		pos=(self.robot.x, self.robot.y)
		while(calcul.distance(pos, coord)>3):
			res=self.robot.avancevers(coord)
			pos=(self.robot.x, self.robot.y)
			time.sleep(0.025)
			self.can.move(self.r, res[0], res[1])
			self.can.update()

	def demo(self):
		self.afficheRobot()	
		self.vers((600,10))
		self.vers((10, 10))
		self.vers((350,300)) 
		self.vers((600,600))
		self.vers((350,350))
		self.vers((400,20))
		self.vers((1,1))
		self.vers((350,350))
		self.vers((200, 100))


# Programme principal
if __name__ == '__main__':
	import numpy as np
	import Arene
	import Robot
	import calcul
	import time
	from tkinter import*												
	#test----------------------------
	robot=Robot.Robot(500, 500, 100, 100)
	arene=Arene.Arene(1000, robot)
	arene.ajouterObstacleAleatoire()
	f = AffichageTK(arene, robot)

