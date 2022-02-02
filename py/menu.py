from py.var import constante

class MENU:
	"""docstring for MENU"""
	def __init__(self,btnplay,btnoption,btnexit):
		self.btns = [btnplay,btnoption,btnexit] 

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