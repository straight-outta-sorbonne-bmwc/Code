class Robot:
    def __init__(self,x,y,longueur,largeur,direction):
        self.x=x
        self.y=y
        self.longueur=longueur
        self.largeur=largeur
        self.direction=direction
        Coordonne=[(self.x,self.y),(self.x+self.longueur,self.y),(self.x+longueur,self.y+largeur),(self.x,self.y+self.largeur)]
