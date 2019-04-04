from threading import Thread
import time

#from simulation import robot, affichage, arene
from simulation import strategie
from robot2I013 import Robot2I013

robot=Robot2I013()
#robot=robot.Robot(500, 500, 50, 50)
#arene=arene.Arene(robot)
#fenetre=affichage.AffichageTK(arene, robot)
#paralelle=Thread(target=fenetre.start_affichage)
#paralelle.start()
strat=strategie.strategie_tourner_droite(360, robot, 500)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()
while not strat.stop():
	#arene.update()
	strat.update()
	time.sleep(0.001)
time.sleep(1)


 	