from sys import path
from dataclasses import dataclass
import os
import pygame
from pygame import display
import display as disp

class Main():

   def main(self):
      """[Start the script of the game]
      """
      display = disp.Display()
      pygame.init()
      
      screen = pygame.display.set_mode((disp.SCREEN_WIDTH, disp.SCREEN_HEIGHT))
      display.principal_menu(screen)
      pygame.display.set_caption("Test jeu")
      
      icon = pygame.image.load('icon.png')
      pygame.display.set_icon(icon)
      disp 
     
      playing = True
      
      while(playing):
         for event in pygame.event.get():
            if (event.type == pygame.QUIT):
               playing = False
         pygame.display.update()


Main().main()