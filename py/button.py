import pygame

class Button:
	def __init__(self,text,width,height,pos,elevation,screen,color,color_top,color_txt):
		self.screen = screen
		self.text = text
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = color_top
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = color
		self.color_txt = color_txt
		self.gui_font = pygame.font.Font(None,30)
		self.text_surf = self.gui_font.render(text,True,self.color_txt)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		self.colors = [color_top,color_txt]

	def draw(self):
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
		pygame.draw.rect(self.screen,self.bottom_color, self.bottom_rect,border_radius = 30)
		pygame.draw.rect(self.screen,self.top_color, self.top_rect,border_radius = 30)
		self.screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.text_surf = self.gui_font.render(self.text,True,self.colors[0])
			self.top_color = self.colors[1]
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = self.colors[0]
			self.text_surf = self.gui_font.render(self.text,True,self.colors[1])







#button1 = Button('Click me',200,40,(200,250),5)
#button1.draw()