import pygame
from py.var import constante

def initialize():
    """
    initialize pygame
    """
    screen = pygame.display.set_mode((constante["width"],constante["height"]), pygame.FULLSCREEN) 
    pygame.display.set_caption(constante['name_of_game'])
    #icon_32x32 = pygame.image.load("icon.ico").convert_alpha() 
    #pygame.display.set_icon(icon_32x32)  
    clock = pygame.time.Clock() 
    ms = clock.tick(constante["fps"]) 
    return screen,clock