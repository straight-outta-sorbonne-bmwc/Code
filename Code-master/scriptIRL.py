
#from simulation import robot, affichage, arene
from simulation import strategie
from threading import Thread
import time
import math
import robot2I013

robot=robot2I013.Robot2I013()
strat=strategie.strategie_carre(robot, 800)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()
while not strat.stop():
	strat.update()
	time.sleep(0.01)
time.sleep(1)