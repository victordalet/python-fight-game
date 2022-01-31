import tkinter,pygame

pygame.init()
root = tkinter.Tk()

################################### CONSTANTES ###################################

constante = {"position_centre":(root.winfo_screenwidth()/2,root.winfo_screenheight()/ 2),"height":root.winfo_screenheight(),
             "width":root.winfo_screenwidth(),"fps":60,"bin_position":(999999,-55555555),'name_of_game':'FIGHT GAME'}

################################### VARIABLES AVEC CODE COULEUR ###################################

colors = {"white":(255, 255, 255),"red":(255, 0, 0),"black":(0, 0, 0),"green":(0, 255, 0),"purple":(170,74,227),"bleu":(22,125,203)}

################################### VARIABLES DES TOUCHES ###################################

touches = {"attack":pygame.key.get_pressed()[pygame.K_SPACE],'top':pygame.key.get_pressed()[pygame.K_w],'down':
            pygame.key.get_pressed()[pygame.K_s],'right':pygame.key.get_pressed()[pygame.K_a],'left':pygame.key.get_pressed()[pygame.K_d]}