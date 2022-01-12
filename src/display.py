import pygame

import os
import time

from pygame import image
from monster import Monster

INTRO = """Lors du première épisode, notre valeureux héro est mort en veins..."""
INTRO1 = """Il n'était pas si valeureux au final."""
INTRO2 = """Mais cette fois ci, arriverez-vous à surmonter nos épreuves ?"""
INTRO3 = """WELCOME TO THE MORTAL KKKKOMBAT ....."""
INTRO4 = """Euh ah nan pardon c'est"""
INTRO5 = """Brightest Dungeon 2 Anniversary Collector Deluxe Edition"""

ENTRER = """Vous entrer dans le donjon"""

GENERIQUE = """\t\tBrightest Dungeon 2 Anniversary Collector Deluxe Edition


\tMerci d'avoir jouer

\tCreé par : Florian et Yanis

\tStory telling :Florian et Yanis

\tGraphisme : Florian et Yanis

\tSon : Florian et Yanis

\tEffet spéciaux : Florian et Yanis

\tActeur principal : Florian

\tFaute d'orthographe : Yanis

\tRemerciement spéciaux : Charles\n"""

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
gris = (192,192,192)
red = (255,0 , 0)
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 900

class Display:
    
    
    def principal_menu(self, screen, select):
        font = pygame.font.Font('font.ttf', 50)
        text = font.render("Brightest Dungeon 2", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 200))
        screen.blit(text, text_rect)
        
        if (select != 1):
            text = font.render("Nouvelle Partie", True, gris)
        else:
            text = font.render("Nouvelle Partie", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 300))
        screen.blit(text, text_rect)
        
        if (select != 2):
            text = font.render("Charger Partie", True, gris)
        else:
            text = font.render("Charger Partie", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 350))
        screen.blit(text, text_rect)
        if (select != 3):
             text = font.render("Credit", True, gris)
        else:
            text = font.render("Credit", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 400))
        screen.blit(text, text_rect)
        
        if (select != 4):
            text = font.render("Quitter", True, gris)
        else:
            text = font.render("Quitter", True, white)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 450))
        screen.blit(text, text_rect)
        
    def display_stats(self, hero):
        """[Print the main stats of the current hero state]

        Args:
            hero ([Object]): [The current hero]
        """
        print('******** Statistiques ******** \n')
        print(f"Niveau : {hero.lvl}")
        print(f"Expérience : {hero.xp} / {hero.xp_lvl_up}")
        print(f"Point de vie : {hero._life[0]} / {hero._life[1]}")
        print(f"Force : {hero._strength}")
        print(f"Armure : {hero._armor}")
        print(f"Chance de coup critique : {hero._crit_rate}\n")
        print('******** ------------ ********\n')
             
    def display_enemies(self, mob_list):
        """[Display the list of enemies in the current stage]

        Args:
            mob_list ([list]): [A list of monster object]
        """
        for mob in mob_list:
            print(f"{mob.rank} : {mob._life[0]} / {mob._life[1]} PV")
        print()
            
    def turn_menu(self, book, strength):
        i = 2
        print("Quel action voulez-vous faire :\n",
                f"1 : Attaque simple ({strength} dmg)")
        nb_spell = book["Heal"][0]
        power = book["Heal"][2]
        print(f" 2 : Utiliser Heal, {nb_spell} Utilisation disponible (+{power} pv)") 
        nb_spell = book["Fire"][0]
        power = book["Fire"][2]
        print(f" 3 : Utiliser Fire, {nb_spell} Utilisation disponible ({power} dmg)")
        nb_spell = book["Lightning"][0]
        power = book["Lightning"][2]
        print(f" 4 : Utiliser Lightning, {nb_spell} Utilisation disponible ({power} dmg)")
        nb_spell = book["Ice"][0]
        power = book["Ice"][2]
        print(f" 5 : Utiliser Ice, {nb_spell} Utilisation disponible ({power} dmg)")
        print(" 6 : Sauvegarder")
        print(" 7 : Quitter")
    
    def story(self, string, screen):
        font = pygame.font.Font('font_story.ttf', 40)
        for i in range(0, len(string)+1):
            time.sleep(0.02)
            background = pygame.image.load('story.jpg')
            screen.blit(background, (0,0))
            text = font.render(string[:i], True, white)
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 450))
            screen.blit(text, text_rect)
            pygame.display.update()
        time.sleep(2)

    def get_image(self, sheet, ligne, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0,0), ((frame * width), (ligne * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)
        return image      
    
    def animation_attack(self, screen, dest_x):
        x = 25
        frame = 5
        background = pygame.image.load('game.jpg')
        sprite_sheet_image = pygame.image.load('Warior.png').convert_alpha()
        for i in range(0, 2):
            while (frame > 0):
                screen.blit(background, (0,0))            
                frame_0 = self.get_image(sprite_sheet_image,i, frame, 270, 270, 1, black)
                screen.blit(frame_0, (x, 470))
                time.sleep(0.05) 
                pygame.display.flip()
                frame -= 1
            frame = 5
        while(x <= dest_x - 70):
            screen.blit(background, (0,0))
            frame_0 = self.get_image(sprite_sheet_image,2, frame, 270, 270, 1, black)
            screen.blit(frame_0, (x, 470))
            x += 20
            time.sleep(0.05) 
            frame -= 1
            if (frame == 0):
                frame = 5
            pygame.display.flip()
        frame = 5
        for i in range(3, 6):
            while (frame > 0):
                screen.blit(background, (0,0))
                frame_0 = self.get_image(sprite_sheet_image,i, frame, 270, 270, 1, black)
                screen.blit(frame_0, (x, 470))
                time.sleep(0.05) 
                pygame.display.flip()
                frame -= 1
            frame = 5
            
            
    def display_game(self, screen):
        self.animation_attack(screen, 900)
        background = pygame.image.load('game.jpg')
        font = pygame.font.Font('font_life.ttf', 23)
        screen.blit(background, (0,0))
        pygame.display.flip()
        life = (150, 200)
        mp = (300, 350)
        monsters = []
        monsters.append(Monster((25, 30), 4, 1, 0, {}, "Gobelin", 1))
        monsters.append(Monster((40, 40), 4, 1, 0, {}, "Gobelin", 1))
        monsters.append(Monster((80, 150), 4, 1, 0, {}, "Archer", 1))
        
        #Display Hero
        sprite_sheet_image = pygame.image.load('Warior.png').convert_alpha()
        frame_0 = self.get_image(sprite_sheet_image,0, 1, 275, 270, 1, black)
        screen.blit(frame_0, (25, 470))
        
        #Display Life
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(35, 0, 125, 30), 2)
        pygame.draw.rect(screen, (180,0, 0), pygame.Rect(37, 1, 121*life[0]/life[1], 27))
        string = str(life[0]) + " / " + str((life[1]))
        text = font.render(string, True, red)
        text_rect = text.get_rect(center=(100, 50))
        screen.blit(text, text_rect)
        
        #Display Mp
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(35, 70, 125, 30), 2)
        pygame.draw.rect(screen, (0,0, 180), pygame.Rect(37, 71, 121*mp[0]/mp[1], 27))
        string = str(mp[0]) + " / " + str((mp[1]))
        text = font.render(string, True, blue)
        text_rect = text.get_rect(center=(100, 120))
        screen.blit(text, text_rect)
        
        #Display monster life
        x = 750
        for info in monsters:
            text = font.render(info.rank, True, white)
            text_rect = text.get_rect(center=(x+65, 820))
            screen.blit(text, text_rect)
            pygame.draw.rect(screen, (180,180,180), pygame.Rect(x, 840, 125, 30), 2)
            pygame.draw.rect(screen, (180,0, 0), pygame.Rect(x+2, 841, 121*info._life[0]/info._life[1], 27))
            string = str(info._life[0]) + " / " + str((info._life[1]))
            text = font.render(string, True, red)
            text_rect = text.get_rect(center=(x+70, 890))
            screen.blit(text, text_rect)
            x += 170
            
        font = pygame.font.Font('font.ttf', 40)
        #Button attack
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(0, 850, 100, 50))
        text = font.render("Attack", True, black)
        text_rect = text.get_rect(center=(50, 880))
        screen.blit(text, text_rect)
        
        #Button magic
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(150, 850, 100, 50))
        text = font.render("Magic", True, black)
        text_rect = text.get_rect(center=(200, 880))
        screen.blit(text, text_rect)
        
        #Button magic
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(300, 850, 150, 50))
        text = font.render("Inventory", True, black)
        text_rect = text.get_rect(center=(375, 880))
        screen.blit(text, text_rect)
        
        #Button menu
        pygame.draw.rect(screen, (180,180,180), pygame.Rect(500, 850, 100, 50))
        text = font.render("Menu", True, black)
        text_rect = text.get_rect(center=(550, 880))
        screen.blit(text, text_rect)
        
        pygame.display.update()
        
        