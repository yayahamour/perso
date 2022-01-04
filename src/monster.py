from dataclasses import dataclass, field
from typing import ClassVar
from character_core_mechanics import CharacterCoreMechanics
import random

GOBLIN_DICT = {"Heal":(0,0,0), "Fire":(0,0,0), "Ice":(0,0,0), "Lightning":(0,0,0)}
@dataclass
class Monster(CharacterCoreMechanics):
    rank: str
    xp: int
    
    def __post_init__(self):
        """[post init the spell book of some type of enemies]
        """
        if self.rank == 'Liche':
            self._book = {"Heal":(0,0,0), "Fire":(999,999,7), "Ice":(0,0,0), "Lightning":(0,0,0)}
            
        if self.rank == 'Drake':
            self._book = {"Heal":(0,0,0), "Fire":(999,999,10), "Ice":(999,999,10), "Lightning":(999,999,10)} 
             
    def turn(self, hero):
        """[handle the turn of the monsters]

        Args:
            hero ([object]): [the player]
        """
        if self.rank == 'Gobelin':
            self.base_attack(hero)
            
        if self.rank == 'Liche':
            r_num = random.randint(1,100)
            if r_num <= 60:
                self.base_attack(hero)
            else:
                self.use_spell('Fire', hero)
                
        if self.rank == 'Orc':
            self.base_attack(hero)
            self.base_attack(hero)
            
        if self.rank == 'Drake':
            r_num = random.randint(1,100)
            if r_num <= 50:
                self.base_attack(hero)
            else:
                self.use_spell('Fire', hero)