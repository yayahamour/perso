import display as disp
import pygame

class Menu :
    
    def principal(self, select, screen):
        display = disp.Display()
        
        display.principal_menu(screen, select)
        pygame.display.set_caption("Brightest Dungeon 2")
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        pygame.display.update()