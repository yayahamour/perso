from dataclasses import dataclass, field
from random import randint

@dataclass
class CharacterCoreMechanics():
    _life : tuple
    _strength : int
    _armor: int
    _crit_rate: int
    _book : dict

    def base_attack(self, target):
        """[this method use the strength of the one who attack and reduce his strength from the target health]

        Args:
            target ([Object]): [An hero object or a monster object]

        Returns:
            [Object]: [An Hero Object or a Monster Object with modified values]
        """
        if(self._strength > 0):
            crit_roll = randint(1,100)
            if crit_roll > self._crit_rate:
                life = target._life[0] - (self._strength - target._armor)
            else:
                life = target._life[0] - ((self._strength * 2 ) - target._armor)
            if (life < 0):
                life = 0
            target._life = (life, target._life[1]) 
        return target
        

    def use_spell(self, spell, target=None):
        """[summary]

        Args:
            spell ([type]): [description]
            target ([type], optional): [An hero object or a monster object]. Defaults to None.
        """
        crit_roll = randint(1,99)
        if(spell == "Heal"):
            if crit_roll > self._crit_rate:
                life = (self._life[0]+self._book[spell][2])
                if (life > self._life[1]):
                    life = self._life[1]
                self._life = (life, self._life[1])
                self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2])
            else:
                life = self._life[0]+ (self._book[spell][2] * 2)
                if (life > self._life[1]):
                    self._life = (self._life[1], self._life[1])
                self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2])
        else:
            if crit_roll > self._crit_rate:
                life = target._life[0] - self._book[spell][2]
                target._life = (life, target._life[1])
                self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2]) 
            else:
                life = target._life[0] - (self._book[spell][2] * 2)
                target._life = (life, target._life[1])
                self._book[spell] = (self._book[spell][0] - 1, self._book[spell][1], self._book[spell][2]) 