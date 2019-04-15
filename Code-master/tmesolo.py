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
#
#IMPORTANT : Toutes les strategies,fonctions etc sont listés dans le fichier tmesolo.txt et sont aussi disponibles sur affichage.py et strategie.py
#
#Exercice 1 Question 1: Voir fichier arene
#Exercice 1 Question 2: Voir fichier arene
#Exercice 2 Question 1:
strat=strategie.strategie_triangle_equi(robot, 200)
#Exercice 2 Question 2:
#strat=strategie.strategie_polygone(robot, 200,20)
#Exercice 2 Question 3:
#strat=strategie.strategie-mur(robot, 200)
thread_strat=Thread(target=strat.update)
thread_strat.start()
strat.start()

while not strat.stop():
	arene.update()
	strat.update()
	time.sleep(0.01)
	#print(robot.x, robot.y)
time.sleep(1)



 	
