import Arene
import Robot

robot=Robot.Robot(5, 5, 40, 10)
arene=Arene.Arene(10, robot)
arene.ajouterObstacleAleatoire()

for i in arene.obstacles:
	print(i.toString())