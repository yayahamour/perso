import pygame

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
gris = (192,192,192)
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 900

class Display:

    def principal_menu(self, screen):
        menu_background = pygame.image.load('fond.jpg')
        screen.blit(menu_background, (0,0))
        pygame.display.update()

        font = pygame.font.Font('font.ttf', 50)
        text = font.render("Brightest Dungeon 2", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 200))
        screen.blit(text, text_rect)
        
        text = font.render("Nouvelle Partie", True, gris)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 300))
        screen.blit(text, text_rect)
        
        text = font.render("Charger Partie", True, gris)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 350))
        screen.blit(text, text_rect)
        
        text = font.render("Credit", True, gris)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 400))
        screen.blit(text, text_rect)
        
        text = font.render("Quitter", True, gris)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 450))
        screen.blit(text, text_rect)