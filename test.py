from os import system
from sys import path
from dataclasses import dataclass
import time
import pygame
path.append("./src")
import display as disp
from menu import Menu
from game import Game

pygame.init()
screen = pygame.display.set_mode((1612, 1612))
menu_background = pygame.image.load('Warior.png')
screen.blit(menu_background, (0,0))
pygame.display.update()
playing = True
while(playing):
    pass