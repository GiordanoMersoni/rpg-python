import random, math
from equip_item import *

class Armor(Equip_item):
    def __init__(self, name, price, DEF):
        super().__init__(name, price)
        self.DEF = DEF
        self.type = 'armor'
    def getDEF(self):
        return self.DEF
    def setDEF(self, DEF):
        self.DEF = DEF

# ----------------------------------------------------------- #

starterArmor = Armor('Starter Armor', 350, (0, 4))

decentArmor = Armor('Decent Armor', 550, (2, 6))
