import pygame
from py.var import constante

class create_obj:
    def __init__(self,src,name):
        self.src = src
        self.name = name
        self.image = pygame.image.load(src).convert_alpha()
        self.image_rectangle = self.image.get_rect()
        self.image_rectangle.center = constante["bin_position"]
        x, y = self.image.get_size()
        new_x,new_y = (constante["width"] * x) /1400, (constante["height"] * y) /800
        self.image = pygame.transform.scale(self.image,(new_x,new_y))
        print(self.name)
    
    def get_image(self):
        return self.image_rectangle,self.image

#######################################################
src = 'assets/'
list_obj = []
#################################
list_frame_soldier = [[src+'soldierframe'+str(i)+'.png','soldierframe'+str(i)] for i in range(1,5)]
list_frame_nurse = [[src+'nurseframe'+str(i)+'.png','nurseframe'+str(i)] for i in range(1,5)]
list_frame_dictator = [[src+'dictatorframe'+str(i)+'.png','dictatorframe'+str(i)] for i in range(1,5)]
list_frame_sergeant = [[src+'sergeantframe'+str(i)+'.png','sergeantframe'+str(i)] for i in range(1,5)]
####################################
list_obj += list_frame_nurse
list_obj += list_frame_soldier
list_obj += list_frame_sergeant
list_obj += list_frame_dictator