import pygame
from py.var import *

class Character:
	def __init__(self,name,weapon,hp_max,damage,list_image,nb):
		self.__name = name
		self.rect = pygame.Rect((20, 50), (50, 100))
		self.__weapon = weapon
		self.__hp_max = hp_max
		self.__hp = hp_max 
		self.__damage = damage
		self.__coordinate = constante['position_centre']
		self.__speed = 10
		self.move = {'top':True,'down':True,'left':True,'right':True}
		self.list_image = list_image
		self.image = list_image[0]
		self.nb = nb
		self.speed_atack = 150
		self.sens = 'right'

	def ft_move(self): 
		"""if (self.nb == 1 and  pygame.key.get_pressed()[pygame.K_z]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_UP]):
			if self.move['top']:
				self.set_coordinate([self.get_coordinate()[0],self.get_coordinate()[1]-self.get_speed()])
		if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_s]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_DOWN]):
			if self.move['down']:
				self.set_coordinate([self.get_coordinate()[0],self.get_coordinate()[1]+self.get_speed()])"""
		if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_q]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_LEFT]):
			if self.move['left']:
				self.set_coordinate([self.get_coordinate()[0]-self.get_speed(),self.get_coordinate()[1]])
		if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_d]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_RIGHT]):
			if self.move['right']:
				self.set_coordinate([self.get_coordinate()[0]+self.get_speed(),self.get_coordinate()[1]])

	def get_coordinate(self):
		return self.__coordinate

	def set_coordinate(self,coordinate):
		self.__coordinate = coordinate

	def go_to(self,x,y):
		self.set_coordinate([x,y])

	def get_hp(self):
		return self.__hp 

	def set_hp(self,hp):
		self.__hp = hp

	def get_damage(self):
		return self.__damage

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
		if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_SPACE]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_RETURN]):
			if self.collision(other):
				other.give_hp(-self.get_damage())
				other.set_coordinate([other.get_coordinate()[0]+self.speed_atack,other.get_coordinate()[1]])

	def wall(self):
		if self.get_coordinate()[0] <= 0 :
			self.move['left'] = False
		else :
			self.move['left'] = True

		if self.get_coordinate()[0] >= constante['width']:
			self.move['right'] = False
		else:
			self.move['right'] = True

		if self.get_coordinate()[0] <= 0:
			self.move['top'] = False
		else:
			self.move['top'] = True

		if self.get_coordinate()[1] >= constante['height']:
			self.move['down'] = False
		else:
			self.move['down'] = True

	def random_position(self):
		self.go_to(random.randint(0,constante['width']),random.randint(0,constante['height']))

	def center_picture(self):
		self.image.center = self.get_coordinate()

	def frame_gestion(self):
		if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_SPACE]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_RETURN]):
			if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_q]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_LEFT]):
				self.image = self.list_image[3]
			if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_d]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_RIGHT]):
				self.image = self.list_image[2]
			else :
				if self.sens == 'right':
					self.image = self.list_image[2]
				else :
					self.image = self.list_image[3]
		else:
			if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_q]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_LEFT]):
				self.image = self.list_image[1]
				self.sens = 'left'
			if (self.nb == 1 and pygame.key.get_pressed()[pygame.K_d]) or (self.nb == 2 and pygame.key.get_pressed()[pygame.K_RIGHT]):
				self.image = self.list_image[0]
				self.sens = 'right'
			else : 
				if self.sens == 'right':
					self.image = self.list_image[0]
				else :
					self.image = self.list_image[1]

	def dead(self,other):
		if self.get_hp() <= 0 :
			self.set_coordinate(list(constante['bin_position']))
			other.set_coordinate(list(constante['bin_position']))
			return False
		return True

	def gestion(self):
		self.rect.center = self.get_coordinate()

######################################################################################################################

class soldier(Character):
	"""docstring for soldier"""

	def __init__(self,name,weapon,hp_max,damage,list_image,nb):
		super().__init__(name,weapon,hp_max,damage,list_image,nb)

	def spe(self):
		pass


class nurse(Character):
	"""docstring for nurse"""

	def __init__(self,name,weapon,hp_max,damage,list_image,nb):
		super().__init__(name,weapon,hp_max,damage,list_image,nb)
		self.__regenerate = 1

	def get_regenerate(self):
		return self.__regenerate 

	def care(self):
		super().give_hp(self.get_regenerate())

	def spe(self):
		self.care()


class dictator(Character):
	"""docstring for dictator"""

	def __init__(self,name,weapon,hp_max,damage,list_image,nb):
		super().__init__(name,weapon,hp_max,damage,list_image,nb)

	def spe(self):
		pass


class sergeant(Character):
	"""docstring for sergeant"""

	def __init__(self,name,weapon,hp_max,damage,list_image,nb):
		super().__init__(name,weapon,hp_max,damage,list_image,nb)

	def spe(self):
		pass