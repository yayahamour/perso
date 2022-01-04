import pygame
import os


class Music():

    def __init__(self) -> None:
        """[Initialize pygame mixer]
        """
        pygame.mixer.init()
      
    def main_music(self):
        """[The main music and file check]
        """
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("Histoire.mp3")
            pygame.mixer.music.play(-1,0,0)
        except:
            os.error("Verifier fichier son")
    
    def victory_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("Victory.mp3")
            pygame.mixer.music.play()
        except:
            os.error("Verifier fichier son")

    def up_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("up.mp3")
            pygame.mixer.music.play()
        except:
            os.error("Verifier fichier son")

    def death_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("death.mp3")
            pygame.mixer.music.play()
        except:
            os.error("Verifier fichier son")
    
    def boss_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("boss.mp3")
            pygame.mixer.music.play()
        except:
            os.error("Verifier fichier son")
    
    def boss_theme_music(self):
        try :
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("boss_theme.mp3")
            pygame.mixer.music.play(-1,0,0)
        except:
            os.error("Verifier fichier son")
