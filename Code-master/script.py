from simulation import *
from threading import Thread
import time

robot=robot.Robot(500, 500, 50, 50)
arene=arene.Arene(robot)
fenetre=affichage.AffichageTK(arene, robot)
paralele=Thread(target=fenetre.start_affichage)
paralele.start()
while not arene.stop:
	arene.update()
	time.sleep(0.2)
	print("test")
time.sleep(1)





