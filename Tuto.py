class Tuto(object):
	longueur = 60	# variable globale qui correspond à la longueur du rectangle
	largeur = 30	# variable globale qui correspond à la largeur du rectangle
	dim = 500		# variable globale qui correspond à la dimension de la fenêtre
	def __init__(self):
		self.root = Tk()							# root variable contenant la fenêtre
		self.root.title('Tuto')						# Nom de la fenêtre	
		self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='white')			# création de la fenêtre 
		self.can.pack()																		# permet l'affcichage de la fenêtre
		self.x0, self.y0 = (self.dim/2)-(self.longueur/2), (self.dim/2)-(self.largeur/2)	# coordonnées du rectangle pour qu'il soit au milieu de la fenêtre
		self.x1, self.y1 = (self.dim/2)+(self.longueur/2), (self.dim/2)+(self.largeur/2)
		self.RectangleMilieu()																# appel de la méthode RectangleMilieu() qui affiche un rectangle dans la fenêtre
		avancer = Button(self.root, text='avancer', command=self.Avancer)					# bouton qui appelera la méthode Avancer() quand on clique dessus
		quitter = Button(self.root, text = 'quitter', command=self.root.quit)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)															# emplacement des boutons
		avancer.pack(side=BOTTOM)
		self.root.mainloop()																# démarre la classe tuto

	def RectangleMilieu(self):
		self.rectangle = self.can.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill='green')	# affiche un rectangle


	def Avancer(self):
		for i in range(10):									# boucle pour faire avancer de 10 pas à chaque appel de la méthode Avancer()
			if(self.Collision(self.x1)):			# Appel de la fonction Collision() pour tester si le robot n'est pas au bord de la fenêtre
				self.x1=self.x1+1							# modifie la variable x1 qui sert de test pour la méthode Collision() car 'self.can.move' ne modifie les varaibles x0, y0, x1, y1
				self.can.move(self.rectangle, 1, 0)			# fait avancer le robot de 1 pas 
			else :
				return										# si l'avant du robot est contre le bord de la fenêtre il ne peut plus avancer

	def Collision(self, x):
		if(x==(self.dim-1)):								# test si le robot est au bord de la fenêtre
			return False
		return True

# Programme principal
if __name__ == '__main__':
	from tkinter import*							
	f = Tuto()					# instanciation de l'objet application