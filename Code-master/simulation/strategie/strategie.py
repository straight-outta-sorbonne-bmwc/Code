
import math 


class strategie_avance:
	def __init__(self, distance, robot, vitesse):
		self.distance=distance
		self.robot=robot
		self.vitesse = vitesse

	def start(self):
		self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
		self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])

	def update(self):

		if self.stop():
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
			return
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT, self.vitesse)
		
	def stop(self):

		l,r=self.robot.get_motor_position()
		res = (l*(self.robot.WHEEL_CIRCUMFERENCE/360) >= self.distance) or (self.robot.get_distance()<7 )
		if res:
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
		return res


class strategie_tourner_gauche:
	def __init__(self, angle, robot, vitesse):
		self.angle=angle
		self.robot=robot
		self.vitesse=vitesse
		self.distance=angle*(math.pi/180)*self.robot.WHEEL_BASE_WIDTH


	def start(self):
		self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
		self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])

	def update(self):
		if self.stop():
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
			return	
		self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, self.vitesse)
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT, 0)

	def stop(self):
		l,r=self.robot.get_motor_position()
		r_rad = r*math.pi/180
		d = r_rad * self.robot.WHEEL_DIAMETER/2
		res =  d >= self.distance or (self.robot.get_distance()< 7)
		if res :
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
		return res


class strategie_tourner_droite:
	def __init__(self, angle, robot, vitesse):
		self.angle=angle
		self.robot=robot
		self.vitesse=vitesse
		self.distance=angle*(math.pi/180)*self.robot.WHEEL_BASE_WIDTH


	def start(self):
		self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT,self.robot.get_motor_position()[0])
		self.robot.offset_motor_encoder(self.robot.MOTOR_RIGHT,self.robot.get_motor_position()[1])

	def update(self):
		if self.stop():
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
			return	
		self.robot.set_motor_dps(self.robot.MOTOR_LEFT, self.vitesse)
		self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)

	def stop(self):
		l,r=self.robot.get_motor_position()
		l_rad = l*math.pi/180
		d = l_rad * self.robot.WHEEL_DIAMETER/2
		res =  d >= self.distance or (self.robot.get_distance()< 7)


		if res :
			self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
		return res


class strategie_carre:
	def __init__(self,robot,vitesse):
		self.robot=robot
		self.vitesse=vitesse
		self.liste=[strategie_avance(200,self.robot,self.vitesse),strategie_tourner_droite(90,self.robot,self.vitesse)]
		self.nb_tour=0
		
	def start(self):
		self.liste[self.nb_tour%2].start()

	def update(self):
		if self.stop():
			return
		
		if self.liste[self.nb_tour%2].stop():
			self.nb_tour+=1
			self.liste[self.nb_tour%2].start()
		
		else:
			self.liste[self.nb_tour%2].update()

	def stop(self):
		return self.nb_tour>=8
		
