from simulation import robot, affichage, arene
from simulation import strategie
from threading import Thread
import time

#import Robot2I013

robot=robot.Robot(500, 500, 50, 50)
arene=arene.Arene(robot)
fenetre=affichage.AffichageTK(arene, robot)
paralelle=Thread(target=fenetre.start_affichage)
paralelle.start()
strat=strategie.strategie_triangle(robot, 100)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()

while not strat.stop():
	arene.update()
	strat.update()
	time.sleep(0.01)
	#print(robot.x, robot.y)
time.sleep(1)



 	
