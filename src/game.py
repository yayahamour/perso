from dataclasses import dataclass, field
import os

from monster import Monster
from hero import Hero
from display import *
from random import randint
import pymongo
from music import Music

@dataclass
class Game():
    player : Hero = Hero((50,50), 5, 0, 5, {"Heal":(3,3,10), "Fire":(0,0,5), "Ice":(0,0,7), "Lightning":(0,0,10)}, 0, 1, 50)
    monsters : list = field(default_factory=list)
    stage : int = 1
    display : Display = Display()   
    music : Music = Music()
   
    def next_stage(self):
        """[The function manage all the stage state]
        """
        self.stage += 1
        self.display.story(f"Vous montez longuement un escalier en collimasson pour arriver à l'étage {self.stage}\n")
        nb = 1
        if (self.stage >= 6 and self.stage % 5 == 1):
            self.display.story("Vous étes en lieu sur, profitez en pour vous reposer\n")
            time.sleep(3)
            self.player.camp()
            drop = randint(1, 100)
            if (drop >= 70):
                self.display.story(OBJET)
                self.display.story("Vous gagnez 1 d'armure")
                self.player._armor += 1
        if ((self.stage % 10) == 0):
            self.music.boss_music()
            self.display.story(FINAL_BOSS)
            self.music.boss_theme_music()
            self.monsters.append(Monster((100,100),10,5,5,{},"Drake", 1000))
        elif ((self.stage % 5) == 0):
            self.music.boss_music()
            self.display.story(FIRST_BOSS)
            self.music.boss_theme_music()
            self.monsters.append(Monster((40,40),3,2,2,{},"Orc", 500))
        else :
            if self.stage > 5 and self.stage < 10:
                nb = 2
            elif self.stage > 10:
                nb = 3
            for i in range(0, nb):
                rand = randint(1,100)
                if(rand >= 70):
                    self.monsters.append(Monster((10,10),1,0,2,{},"Liche", 40))
                else:
                    self.monsters.append(Monster((5,5),2,0,1,{},"Gobelin", 25))

    def game(self):
        """[this function launch the sounds and quit the gme if player has 0 pv]
        """
        playing = True
        turn_player = True
        time_before_loose = 0
        while (playing):
            if (len(self.monsters) == 0):
                try:
                    self.music.victory_music()
                except:
                    os.error("Verifier fichier son")
                self.next_stage()
            while(turn_player and time_before_loose < 4 and playing):
                os.system("cls")
                self.display.display_stats(self.player)
                print(f"Etage : {self.stage}")
                self.display.display_enemies(self.monsters)
                self.display.turn_menu(self.player._book, self.player._strength)
                _input = input("Choix : ")
                try:
                    case = int(_input)
                    if(case != 6) and (case != 7):
                        os.system("cls")
                        if(self.player.turn(case, self.monsters)):
                            turn_player = False
                            time_before_loose = 0
                        else:
                            time_before_loose += 1
                    elif(case == 6):
                        os.system("cls")
                        self.save()
                    elif(case == 7):
                        os.system("cls")
                        playing = False
                except:
                    time_before_loose += 1
            for monster in self.monsters:
                monster.turn(self.player)
            turn_player = True
            if(self.player._life[0] <= 0):
                os.system("cls")
                self.music.death_music()
                self.display.story("YOU DIED !!")
                time.sleep(3)
                self.music.main_music()
                self.display.story(GENERIQUE)
                playing = False
        
    def start(self, screen):
        """[This function start a new game]
        """
        self.music.main_music()
        background = pygame.image.load('story.jpg')
        self.display.story(INTRO, screen)
        self.display.story(INTRO1, screen)
        self.display.story(INTRO2, screen)
        self.display.story(INTRO3, screen)
        self.display.story(INTRO4, screen)
        self.display.story(ENTRER, screen)
        self.display.story(STAGE_1, screen)
        self.player = Hero((50,50), 5, 0, 5, {"Heal":(3,3,10), "Fire":(0,0,5), "Ice":(0,0,7), "Lightning":(0,0,10)}, 0, 1, 50)
        self.monsters = []
        self.stage  = 1
        self.monsters.append(Monster((3, 3), 4, 1, 0, {}, "Gobelin", 1))
        self.game()

    def getDatabase(self):
        """[This function link a var to the database]

        Returns:
            [Document]: [Return the database]
        """
        my_client = pymongo.MongoClient('mongodb://localhost:27017/')
        my_db = my_client['playersaves']
        return my_db
        
    def save(self):
        save_name = input('Choisir un nom pour votre sauvegarde :')
        
        character = { 
            "id" : save_name,
            "life": self.player._life, 
            "strength": self.player._strength, 
            "armor": self.player._armor, 
            "crit": self.player._crit_rate,
            "book": self.player._book,
            "xp": self.player.xp,
            "lvl": self.player.lvl,
            "xplvlup": self.player.xp_lvl_up,
        }
        
        stage = {
            "id" : save_name,
            "stage": self.stage,
        }
        
        my_db = self.getDatabase()
        my_character = my_db['character']
        my_stage = my_db['stage']
        my_monsters = my_db['monsters']
         
        check_id = my_character.find_one({'id': save_name})
        
        if check_id == None:
            my_character.insert_one(character)
            my_stage.insert_one(stage)
            monsters = []
            cnt = 0
            for i in self.monsters:
                monsters.append({
                    "id" : save_name,
                    "id_m": cnt,
                    "life": i._life, 
                    "strength": i._strength, 
                    "armor": i._armor, 
                    "crit": i._crit_rate,
                    "rank": i.rank,
                    "xp": i.xp,
                })
                cnt += 1
            my_monsters.insert_many(monsters)
            
            return my_character.find_one({'id': save_name}) != None
        else:
            my_character.replace_one({'id': save_name}, character)
            my_stage.replace_one({'id': save_name}, stage)
            cnt = 0
            for i in self.monsters:
                monster = ({
                    "id" : save_name,
                    'id_m': cnt,
                    "life": i._life, 
                    "strength": i._strength, 
                    "armor": i._armor, 
                    "crit": i._crit_rate,
                    "rank": i.rank,
                    "xp": i.xp,
                })
                my_monsters.replace_one({'id': save_name, 'id_m': cnt}, monster)
                cnt += 1 
            return my_character.find_one({'id': save_name}) != None
        
    def load(self, save_name):
        """[load a saved game, get all needed data from the database and start the game]

        Args:
            save_name ([string]): [save id]
        """
        my_db = self.getDatabase()
        my_character = my_db['character']
        my_stage = my_db['stage']
        my_monsters = my_db['monsters']

        tmp_hero = my_character.find_one({'id': save_name})

        hero = Hero((tmp_hero['life'][0], tmp_hero['life'][1]), 
                    tmp_hero['strength'], 
                    tmp_hero['armor'],
                    tmp_hero['crit'],
                    {'Heal': (tmp_hero['book']['Heal'][0], tmp_hero['book']['Heal'][1], tmp_hero['book']['Heal'][2]),
                     'Fire': (tmp_hero['book']['Fire'][0], tmp_hero['book']['Fire'][1], tmp_hero['book']['Fire'][2]),
                     'Ice': (tmp_hero['book']['Ice'][0], tmp_hero['book']['Ice'][1], tmp_hero['book']['Ice'][2]),
                     'Lightning': (tmp_hero['book']['Lightning'][0], tmp_hero['book']['Lightning'][1], tmp_hero['book']['Lightning'][2]),
                    },
                    tmp_hero['xp'],
                    tmp_hero['lvl'],
                    tmp_hero['xplvlup']
                    )
        tmp_stage = my_stage.find_one({'id': save_name})
        stage = tmp_stage['stage']
        monsters = []
        tmp_monsters = my_monsters.find({'id': save_name})
        for i in tmp_monsters:
            monsters.append(Monster(
                (i['life'][0], i['life'][1]), 
                i['strength'], 
                i['armor'],
                i['crit'],
                {},
                i['rank'],
                i['xp']
            ))
        self.player = hero
        self.stage = stage
        self.monsters = monsters
        self.music.main_music()
        self.game()
    
    def delete_save(self, save_name):
        
        my_db = self.getDatabase()
        my_character = my_db['character']
        my_stage = my_db['stage']
        my_monsters = my_db['monsters']
        
        my_character.find_one({'id': save_name})
        
        if my_character != None:
            my_character.delete_one({'id': save_name})
            my_stage.delete_one({'id': save_name})
            my_monsters.delete_many({'id': save_name})
            
        return my_character.find_one({'id': save_name}) == None
