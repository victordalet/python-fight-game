from py.var import constante
from py.character import *
import random

class MENU:
	"""docstring for MENU"""
	def __init__(self,btnplay,btnoption,btnexit):
		self.btns = [btnplay,btnoption,btnexit] 
		self.character = ['soldier','dictator','murse','sergeant']
		self.choice_character = []

	def display_button(self):
		for i in self.btns:
			i.draw()

	def close_btn(self):
		for i in self.btns:		
			i.bottom_rect = constante['bin_position']
			i.top_rect = constante['bin_position']

	def click_button(self):
		if dic_button["button_exit"].top_rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0]:
				give_data('../web/json/lancement.json',False)
				pygame.quit()

	def ft_choice_character(self,list_obj_create):
		self.choice_character  = [random.choice(self.character),random.choice(self.character)]
		for i in range(len(self.choice_character)):
			if self.choice_character[i] == 'soldier':
				if i == 0:
					self.choice_character[i] = soldier('1','gun',1000,20,[list_obj_create[0][0],list_obj_create[1][0],list_obj_create[2][0],list_obj_create[3][0]],1)
				else : 
					self.choice_character[i] = soldier('2','gun',1000,20,[list_obj_create[0][0],list_obj_create[1][0],list_obj_create[2][0],list_obj_create[3][0]],2)
			elif self.choice_character[i] == 'dictator':
				if i == 0:
					self.choice_character[i] = dictator('1','gun',1000,20,[list_obj_create[4][0],list_obj_create[5][0],list_obj_create[6][0],list_obj_create[7][0]],1)
				else : 
					self.choice_character[i] = dictator('2','gun',1000,20,[list_obj_create[4][0],list_obj_create[5][0],list_obj_create[6][0],list_obj_create[7][0]],2)
			elif self.choice_character[i] == 'murse':
				if i == 0:
					self.choice_character[i] = nurse('1','gun',1000,20,[list_obj_create[8][0],list_obj_create[9][0],list_obj_create[10][0],list_obj_create[11][0]],1,)
				else : 
					self.choice_character[i] = nurse('2','gun',1000,20,[list_obj_create[8][0],list_obj_create[9][0],list_obj_create[10][0],list_obj_create[11][0]],2)
			elif self.choice_character[i] == 'sergeant':
				if i == 0:
					self.choice_character[i] = sergeant('1','gun',1000,20,[list_obj_create[12][0],list_obj_create[13][0],list_obj_create[14][0],list_obj_create[15][0]],1)
				else : 
					self.choice_character[i] = sergeant('2','gun',1000,20,[list_obj_create[12][0],list_obj_create[13][0],list_obj_create[14][0],list_obj_create[15][0]],2)
		return self.choice_character