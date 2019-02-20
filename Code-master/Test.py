import Arene
import Robot


robot = Robot.Robot(5.0,5.0,10,10)
carre = Arene.Arene(10, robot)
carre.ajouterObstacleAleatoire()
carre.EcritureFichier("fichier.txt")
#carre.LectureFichier("fichier.txt")
