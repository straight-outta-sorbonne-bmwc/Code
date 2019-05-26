from simulation import robot, affichage, arene
from simulation import strategie
from threading import Thread
import time
import math

#import Robot2I013

robot=robot.Robot(500, 500, 50, 50)
arene=arene.Arene(robot)
arene.ajouter_obstacle_aleatoire()

fenetre=affichage.AffichageTK(arene)
paralelle=Thread(target=fenetre.start_affichage)
paralelle.start()
strat=strategie.strategie_carre(robot, 200)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()

while not strat.stop():
	arene.update()
	strat.update()
	time.sleep(0.01)
	
	#print(robot.x, robot.y)
time.sleep(1)



 	
