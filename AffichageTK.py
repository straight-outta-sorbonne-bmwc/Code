class AffichageTK(Objet):
	dim = 500										# variable globale qui correspond à la dimension de la fenêtre
	def __init__(self, arene):
		self.arene=arene
		self.root = Tk()							# root variable contenant la fenêtre
		self.root.title('Tuto')						# Nom de la fenêtre	
		self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='white')			# création de la fenêtre 
		self.can.pack()																		# permet l'affcichage de la fenêtre																		
		quitter = Button(self.root, text = 'quitter', command=self.root.quit)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)															# emplacement des boutons
		self.root.mainloop()

# Programme principal
if __name__ == '__main__':
	from tkinter import*							
	f = Tuto()					# instanciation de l'objet application