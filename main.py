from os import system
from sys import path
from dataclasses import dataclass
import time
import pygame
from pygame import display
import display as disp
from menu import Menu

class Main():

   def main(self):
      """[Start the script of the game]
      """
      select = 1
      menu = Menu()
      pygame.init()
      menu.principal(select)
      playing = True
      while(playing):
         for event in pygame.event.get():
            if (event.type == pygame.QUIT):
               playing = False
               pygame.quit()
               exit()
         keys = pygame.key.get_pressed()
         if keys[pygame.K_UP]:
            select -= 1
            if (select == 0):
               select = 4
            menu.principal(select)
         if keys[pygame.K_DOWN]:
            select += 1
            if (select == 5):
               select = 1
            menu.principal(select)
         time.sleep(0.07)


Main().main()