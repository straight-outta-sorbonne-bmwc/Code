
class AffichageTK(object):
	dim = 10				# variable globale qui correspond à la dimension de la fenêtre
	echelle=25				# à l'échelle x25 sur la fenêtre tkinter	
	tabx=[]
	taby=[]
	k=0
	def __init__(self, arene):
		self.arene=arene
		self.root = Tk()							# root variable contenant la fenêtre
		self.root.title('Tuto')						# Nom de la fenêtre	
		self.can = Canvas(self.root, width=self.dim, height=self.dim, bg='white')			# création de la fenêtre 
		self.can.pack()																		# permet l'affcichage de la fenêtre																		
		quitter = Button(self.root, text = 'quitter', command=self.root.quit)				# bouton pour quitter la fenêtre
		quitter.pack(side=BOTTOM)															# emplacement des boutons
		self.root.mainloop()

	def coordObstacle(self, arene): #On récupére les coordonnées des obstacle
	    for i in range(arene.taille):
	        for j in range(arene.taille):
	            if(arene.Matrice[i][j]==1):
	                self.tabx.append(j)
	                self.taby.append(i)
    

	def afficheObstacle(self):
	    self.k
	    canvas.create_rectangle(self.tabx[self.k]*self.echelle,self.taby[self.k]*self.echelle,self.tabx[self.k]*self.echelle+self.echelle,self.taby[self.k]*self.echelle+self.echelle,fill='red')
	    self.k=self.k+1

# Programme principal
if __name__ == '__main__':
	import numpy as np
	import Arene
	from tkinter import*												
	#test----------------------------
	arene=Arene.Arene(dim)
	arene.ajouterObstacleAleatoire()
	print(arene.Matrice)
	f = Tuto(arene)
	f.coordObstacle(arene)
#---------------------------------
