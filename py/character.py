import pygame
from var import *

class Character:
	"""docstring for Character"""
	def __init__(self,name,weapon,hp_max,damage):
		self.__name = name
		self.rect = pygame.Rect((20, 50), (50, 100))
		self.__weapon = weapon
		self.__hp_max = hp_max
		self.__hp = hp_max 
		self.__damage = damage
		self.__coordinate = [0,0]
		self.__speed = 10
		self.move = {'top':True,'down':True,'left':True,'right':True}

	def move(self):
		if touches['top']:
			if self.move['top']:
				self.get_coordinate(self.get_coordinate()[0],self.get_coordinate()[1]-self.get_speed())
		if touches['down']:
			if self.move['down']:
				self.get_coordinate(self.get_coordinate()[0],self.get_coordinate()[1]+self.get_speed())
		if touches['left']:
			if self.move['left']:
				self.get_coordinate(self.get_coordinate()[0]-self.get_speed(),self.get_coordinate()[1])
		if touches['right']:
			if self.move['right']:
				self.get_coordinate(self.get_coordinate()[0]+self.get_speed(),self.get_coordinate()[1])

	def get_coordinate(self):
		return self.__coordinate

	def set_coordinate(self,[x,y]):
		self.__coordinate = [x,y]

	def go_to(self,x,y):
		self.set_coordinate([x,y])

	def get_hp(self):
		return self.__hp 

	def set_hp(self,hp):
		self.__hp = hp

	def give_hp(self,hp):
		self.__hp += hp

	def get_speed(self):
		return self.__speed

	def set_speed(self,speed):
		self.__speed = speed

	def collision(self,other):
		if self.rect.colliderect(other.rect):
			return True
		return False

	def attack(self,other):
		if touches['attack']:
			if self.collision(other):
				other.give_hp(-attack)

	def wall(self):
		if self.x <= 0 :
			self.move['left'] = False
		else :
			self.move['left'] = True

		if self.x >= constante['width']:
			self.move['right'] = False
		else:
			self.move['right'] = True

		if self.y <= 0:
			self.move['top'] = False
		else:
			self.move['top'] = True

		if self.y >= constante['height']:
			self.move['down'] = False
		else:
			self.move['down'] = True

	def random_position(self):
		self.go_to(random.randint(0,constante['width']),random.randint(0,constante['height']))


######################################################################################################################

class soldier(Character):
	"""docstring for soldier"""

	def __init__(self,name,weapon,hp_max,damage):
		super.__init__(name,weapon,hp_max,damage)

		
class nurse(Character):
	"""docstring for nurse"""

	def __init__(self,name,weapon,hp_max,damage):
		super.__init__(name,weapon,hp_max,damage)
		self.__regenerate = 10

	def get_regenerate(self):
		return self.__regenerate 

	def care(self):
		super.give_hp(self.get_regenerate())

class dictator(Character):
	"""docstring for dictator"""

	def __init__(self,name,weapon,hp_max,damage):
		super.__init__(name,weapon,hp_max,damage)


class sergeant(Character):
	"""docstring for sergeant"""

	def __init__(self,name,weapon,hp_max,damage):
		super.__init__(name,weapon,hp_max,damage)