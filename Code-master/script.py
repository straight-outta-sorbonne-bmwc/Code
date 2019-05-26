#from simulation import robot, affichage, arene
from simulation import strategie
from threading import Thread
import time
import math

import robot2I013

robot=robot2I013.Robot2I013()
#arene=arene.Arene(robot)

#arene.ajouter_obstacle_aleatoire()
#fenetre=affichage.AffichageTK(arene, robot)
#paralelle=Thread(target=fenetre.start_affichage)
#paralelle.start()
strat=strategie.strategie_carre(robot, 800)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()
while not strat.stop():
	#arene.update()
	strat.update()
	time.sleep(0.01)
	
	#print(robot.x, robot.y)
time.sleep(1)



 	
