import pygame ,sys
from py.var import *
from py.base import initialize
from py.character import * 
from py.menu import MENU
from py.button import Button
from py.screen import *
from py.assets import *
from py.action import *

def main():
    pygame.init()
    screen, clock = initialize()
    list_obj_create = []
    for i in list_obj:
        image =  create_obj(i[0],i[1])
        list_obj_create += [image.get_image()]
    print(list_obj_create)
    menus = MENU(Button('PLAY', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]-40), 0, screen, colors['grey'], colors['purple'], colors['white']),
                 Button('OPTION', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]+40), 0, screen, colors['grey'], colors['purple'], colors['white']),
                 Button('EXIT', 200, 40, (constante['position_centre'][0]-100,constante['position_centre'][1]+120), 0, screen, colors['grey'], colors['purple'], colors['white']))
    p1,p2 = menus.ft_choice_character(list_obj_create)
    p1.set_coordinate([20,500])
    p2.set_coordinate([800,500])
    perso = [p1,p2]
    click = True
    while 42:
        ms = clock.tick(constante["fps"])
        print("nombre de fps= {}".format(ms))
        key = pygame.key.get_pressed()
        if click:
            play,click = click_button(menus)
        if play:
            p1.attack(p2)
            p2.attack(p1)
            play = p1.dead(p2)
            play = p2.dead(p1)
            for i in perso:
                i.ft_move()
                i.wall()
                i.frame_gestion()
                i.center_picture()
                i.gestion()
                i.spe()
                print(i.get_coordinate())
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (
                    key[pygame.K_LALT] or key[pygame.K_LALT])):
                pygame.quit()
                sys.exit()
        ###############################################################################################
       	screen_update(screen,menus,[p1,p2],list_obj_create,[p1.get_hp(),p2.get_hp()],[p1,p2])

main()