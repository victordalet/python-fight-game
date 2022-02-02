import pygame
from py.var import *
from py.base import initialize
from py.character import * 
from py.menu import MENU
from py.button import Button
from py.screen import *

def main():
    pygame.init()
    screen, clock = initialize()
    p1 = Character('1','gun',1000,20)
    p2 = Character('2','gun',1000,20)
    menus = MENU(Button('PLAY', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]-40), 0, screen, colors['grey'], colors['purple'], colors['white']),
                 Button('OPTION', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]+40), 0, screen, colors['grey'], colors['purple'], colors['white']),
                 Button('EXIT', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]+120), 0, screen, colors['grey'], colors['purple'], colors['white']))
    while 42:
        ms = clock.tick(constante["fps"])
        print("nombre de fps= {}".format(ms))
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (
                    key[pygame.K_LALT] or key[pygame.K_LALT])):
                pygame.quit()
        ###############################################################################################
       	screen_update(screen,menus,[p1,p2])

main()