import display as disp
import pygame

class Menu :
    
    def principal(self, select):
        display = disp.Display()
        screen = pygame.display.set_mode((disp.SCREEN_WIDTH, disp.SCREEN_HEIGHT))
        display.principal_menu(screen, select)
        pygame.display.set_caption("Test jeu")
        icon = pygame.image.load('icon.png')
        pygame.display.set_icon(icon)
        pygame.display.update()