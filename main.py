from os import system
from sys import path
from dataclasses import dataclass
import time
import pygame
path.append("./src")
import display as disp
from menu import Menu
from game import Game
class Main():
   def display_save(self):
      """[Display all saves]

      Returns:
          [list]: [list of save id]
      """
      my_client = pymongo.MongoClient('mongodb://localhost:27017/')
      my_db = my_client['playersaves']
      my_character = my_db['character']
      my_saves = my_character.find({}, {'id':1, '_id':0})
      cnt = 0
      tab_id = []
      os.system("cls")
      for i in my_saves:
         cnt += 1
         tab_id.append(i['id'])
         print(f"{cnt} : {tab_id[cnt-1]}")
      print(f'{cnt + 1}: Annuler')
      return tab_id
   
   def main(self):
      """[Start the script of the game]
      """
      select = 1
      menu = Menu()
      pygame.init()
      screen = pygame.display.set_mode((disp.SCREEN_WIDTH, disp.SCREEN_HEIGHT))
      menu_background = pygame.image.load('fond.jpg')
      screen.blit(menu_background, (0,0))
      pygame.display.update()
      menu.principal(select, screen)
      playing = True
      game = Game()
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
            menu.principal(select, screen)
         if keys[pygame.K_DOWN]:
            select += 1
            if (select == 5):
               select = 1
            menu.principal(select, screen)
         if keys[pygame.K_RETURN]:
            if (select == 1):
               game.start(screen)
            elif (select == 2):
               pass
            elif (select == 3):
               pass
            else :
               playing = False
               pygame.quit()
         time.sleep(0.09)


Main().main()