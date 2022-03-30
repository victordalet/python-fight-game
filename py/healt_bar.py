import pygame

class Health_bar(pygame.sprite.Sprite):
	def __init__(self,screen,position):
		super().__init__()
		self.position = position
		self.screen = screen
		self.current_health = 200
		self.target_health = 500
		self.max_health = 1000
		self.health_bar_length = 400
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 5

	def get_damage(self,amount):
		if self.target_health > 0:
			self.target_health -= amount
		if self.target_health < 0:
			self.target_health = 0

	def get_health(self,amount):
		if self.target_health < self.max_health:
			self.target_health += amount
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self):
		self.advanced_health()
		
	def basic_health(self):
		pygame.draw.rect(self.screen,(255,0,0),(self.position[0],self.position[1],self.target_health / self.health_ratio,25))
		pygame.draw.rect(self.screen,(255,255,255),(self.position[0],self.position[1],self.health_bar_length,25),4)

	def advanced_health(self):
		transition_width = 0
		transition_color = (255,0,0)

		if self.current_health < self.target_health:
			self.current_health += self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (0,255,0)

		if self.current_health > self.target_health:
			self.current_health -= self.health_change_speed 
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (255,255,0)

		health_bar_width = int(self.current_health / self.health_ratio)
		health_bar = pygame.Rect(self.position[0],self.position[1],health_bar_width,25)
		transition_bar = pygame.Rect(health_bar.right,self.position[1],transition_width,25)
		
		pygame.draw.rect(self.screen,(255,0,0),health_bar)
		pygame.draw.rect(self.screen,transition_color,transition_bar)	
		pygame.draw.rect(self.screen,(255,255,255),(self.position[0],self.position[1],self.health_bar_length,25),4)	



#player.sprite.get_damage(200)
#player.sprite.get_health(200)