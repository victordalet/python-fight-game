import pygame
from py.var import colors,constante

def screen_update(screen,menus,perso):
    screen.fill(colors["black"])
    ##############################################
    menus.display_button()  
    ##############################################
    label_hp_perso1 = pygame.font.Font(None,30).render('hp : '+str(perso[0].get_hp()), 1, colors["bleu"])
    screen.blit(label_hp_perso1, (constante['width']/2-100,10))
    label_hp_perso2 = pygame.font.Font(None,30).render('hp : '+str(perso[1].get_hp()), 1, colors["red"])
    screen.blit(label_hp_perso2, (constante['width']/2+100,10))
    ##############################################
    pygame.display.update()