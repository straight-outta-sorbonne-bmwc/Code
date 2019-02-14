import Arene
import Robot

robot = Robot.Robot(5, 5)
carre = Arene.Arene(10, robot)
carre.ajouterObstacleAleatoire()
print(carre.Matrice)
print("\n")
carre.EcritureFichier("fichier.txt")
carre.LectureFichier("fichier.txt")
print(carre.Matrice)
print("\n")
