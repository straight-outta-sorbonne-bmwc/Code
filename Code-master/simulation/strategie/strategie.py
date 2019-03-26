# from robot import Robot
# from arene import Arene
# from affichage import AffichageTK
# from controleur import Controleur

# robot = Robot()
# arene = Arene(robot)
# controleur = Controleur(robot)ls

# visu = AffichageTK(robot)

# def run(controleur):
# 	while not controleur.stop():
# 		controleur.update()
# 		time.sleep(DT)
import math 


class strategie_avance:
	def __init__(self, distance, robot, vitesse):
		self.distance=distance
		self.robot=robot

	def start(self):
		self.robot.offset_motor_encode(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
		self.robot.offset_motor_encode(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])

	def update(self):
		if self.stop():
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
			return
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT, self.vitesse)
		
	def stop(self):
		l,r=self.robot.get_motor_position()
		res = l*(self.robot.WHEEL_CIRCUMFERENCE/360) >= distance
		if res: 
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
		return res


class strategie_tourner_gauche:
	def __init__(self, angle, robot, vitesse):
		self.angle=angle
		self.robot=robot
		self.vitesse=vitesse

	def start(self):
		self.robot.offset_motor_encode(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
		self.robot.offset_motor_encode(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])

	def uptdate(self):
		if self.stop():
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
			return
		self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.vitesse)
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT, 0)

	def stop(self):
		l,r=l,r=self.robot.get_motor_position
		res = r*((self.robot.WHEEL_BASE_WIDTH*2*math.pi)/360) >= 90*((self.robot.WHEEL_BASE_WIDTH*2*math.pi)/360)
		if res :
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
		return res


