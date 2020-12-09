from equip_item import Equip_item

class Weapon(Equip_item):
    def __init__(self, name, price, ATK):
        super().__init__(name, price)
        self.ATK = ATK
    def getATK(self):
        return self.ATK
    def setATK(self, ATK):
        self.ATK = ATK

class Axe(Weapon):
    def __init__(self, name, price, ATK):
        super().__init__(name, price, ATK)
        self.type = 'axe' 

class Bow(Weapon):
    def __init__(self, name, price, ATK):
        super().__init__(name, price, ATK)
        self.type = 'bow'

class Spear(Weapon):
    def __init__(self, name, price, ATK):
        super().__init__(name, price, ATK)
        self.type = 'spear' 

# ------------------------------------------------------------------- #


starterAxe = Axe('Starter Axe', 350, [6, 15])

starterBow = Bow('Starter Bow', 350, 10)

starterSpear = Spear('Starter Spear', 350, [8, 13])

decentAxe = Axe('Decent Axe', 550, [9, 18])

decentBow = Bow('Decent Bow', 550, 14)

decentSpear = Spear('Decent Spear', 550, [11, 16])




