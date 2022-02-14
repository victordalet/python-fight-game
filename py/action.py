import pygame,sys
from py.var import constante

def click_button(menu):
	if menu.btns[2].pressed : 
		pygame.quit()
		sys.exit() 

	if menu.btns[0].pressed : 
		for i in menu.btns:
			i.top_rect.center = constante['bin_position']
		return True,False
	return False,True
