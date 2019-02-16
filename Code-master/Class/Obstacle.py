class Obstacle:
	largeur = 100
	longueur = 100
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def toString(self):
		return "["+str(self.x)+" ; "+str(self.y)+"]"