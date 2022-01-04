import pygame

import os
import time

INTRO = """Lors du première épisode, notre valeureux héro est mort en veins..."""
INTRO1 = """Il n'était pas si valeureux en faite."""
INTRO2 = """Mais cette fois ci, arriverez-vous à surmonter nos épreuves ?"""
INTRO3 = """WELCOME TO THE MORTAL KKKKOMBAT ....."""
INTRO4 = """Euh ah nan c'est Brightest Dungeon 2 Anniversary Collector Deluxe Edition"""

ENTRER = """Vous avez décidez de vous aventurez dans ce donjon comme bien d'autre aventurier avant vous
peut-être aurez-vous plus de chance"""

OBJET = """Visiblement un de vos prédécesseurs vous à laissé quelque chose\n"""

STAGE_1 = """Un Goblin vous acceuil, c'est votre jour de chance mais méfiez vous
Les prochains étages ne seront surement pas aussi facile\n"""

FIRST_BOSS = """Un Orc se dresse devant vous, je vous avez prévenu\n"""

FINAL_BOSS = """U..UUUNN... UUUUNNNN DRAAAAAAGGGGOONNNN FUUUUYYYEEZZZ\n"""

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
blue = (0, 0, 128)
black = (0, 0, 0)
gris = (192,192,192)
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
        for i in range(0, len(string)):
            time.sleep(0.02)
            background = pygame.image.load('story.jpg')
            screen.blit(background, (0,0))
            text = font.render(string[:i], True, white)
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, 450))
            screen.blit(text, text_rect)
            pygame.display.update()
        time.sleep(2)