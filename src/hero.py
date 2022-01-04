from dataclasses import dataclass
import time

from pygame.mixer import fadeout
from character_core_mechanics import CharacterCoreMechanics
import os
from monster import Monster
from music import Music
@dataclass
class Hero(CharacterCoreMechanics):
    xp: int
    lvl: int
    xp_lvl_up: int
    
    def camp(self) -> dict:
        """[Restore the player health and all stack of spell]

        Returns:
            dict: [the spell book]
        """
        spell_max = self._book['Heal'][1]
        power = self._book['Heal'][2]
        self._book['Heal'] = (spell_max, spell_max, power)

        spell_max = self._book['Fire'][1]
        power = self._book['Fire'][2]
        self._book['Fire'] = (spell_max, spell_max, power)

        spell_max = self._book['Ice'][1]
        power = self._book['Ice'][2]
        self._book['Ice'] = (spell_max, spell_max, power)

        spell_max = self._book['Lightning'][1]
        power = self._book['Lightning'][2]
        self._book['Lightning'] = (spell_max, spell_max, power)
        
        self._life = (self._life[1],self._life[1])
                
    def lvl_up(self) -> dict:
        """[add a lvl to the hero and upgrade his stats]
        """
        self.lvl += 1
        max_life = self._life[1]
        current_life = self._life[0]
        self._life = (current_life, max_life + 5)
        self._strength += 1
        self._crit_rate += 1
        
        if self.lvl == 2:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 6)
            
        if self.lvl == 4:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 6)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 8)   
              
        if self.lvl == 6:
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 8)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 9) 
              
            max_use = self._book['Lightning'][1] + 1
            self._book['Lightning'] = (max_use, max_use, 12)   
            
        if self.lvl == 8:
            self._strength += 4
            self._crit_rate += 10
            
            max_use = self._book['Fire'][1] + 1
            self._book['Fire'] = (max_use, max_use, 12)
            
            max_use = self._book['Ice'][1] + 1
            self._book['Ice'] = (max_use, max_use, 15) 
              
            max_use = self._book['Lightning'][1] + 1
            self._book['Lightning'] = (max_use, max_use, 18) 
            
            max_life = self._life[1]
            current_life = self._life[0]
            self._life = (current_life, max_life + 15)
        
    def add_xp(self, monster) -> int:
        """[this function add the xp form a monster to the xp of the hero]

        Args:
            monster ([object]): [a mob]
        """
        self.xp += monster.xp
        up = False
        while (self.xp >= self.xp_lvl_up):
            up = True
            self.lvl_up()
            print(f"Vous avez gagner un niveau, vous êtes niveau {self.lvl}")
            self.xp_lvl_up += 50 + (self.lvl * 10)
        if (up):
            try:
                music = Music()
                music.up_music()
                time.sleep(5)
            except:
                os.error("Verifier fichier son")
            music.main_music()
        
    def cible(self, monsters):
        """[handle the targeting system in combat]

        Args:
            monsters ([object]): [a mob]
        """
        good = True
        while (good):
            cnt = 1
            for monster in monsters:
                print(f" {cnt} {monster.rank} : {monster._life} pv")
                cnt+=1
            try:
                cible = int(input("Quel enemie voulez-vous cibler : "))
                if (cible > cnt or cible < 0):
                    print("Entrer valeur correct")
                    good = False
                elif(cible < cnt):
                    return cible
            except:
                os.system("cls")
                good = False
        return False

    def turn(self, _input, monsters) -> list:
        """[when the hero turn start, show the hero's possibilities]

        Args:
            _input ([int]): [player choice]
            monsters ([object]): [a mob]
        """
        target = None
        if(_input != 2):
            temp = self.cible(monsters)
            if(isinstance(temp, bool)):
                return False
            else:
                target = monsters[temp-1]
        if _input == 1:
            self.base_attack(target)
            
        elif _input == 2:
            if self._book['Heal'][0] > 0:
                self.use_spell('Heal')
            else:
                return False
            
        elif _input == 3:
            if self._book['Fire'][0] > 0:
                self.use_spell('Fire', target)
            else:
                return False
            
        elif _input == 5:
            if self._book['Ice'][0] > 0:
                self.use_spell('Ice', target)
            else:
                return False
            
        elif _input == 4:
            if self._book['Lightning'][0] > 0:
                self.use_spell('Lightning', target)
            else:
                return False
        if(isinstance(target, Monster)):
            if(target._life[0]<=0):
                    self.add_xp(target)
                    monsters.remove(target)
        return True
