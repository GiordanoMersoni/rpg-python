import random, math, os
from weapon import *
from armor import *

class Char:
    def __init__(self, name, armor, weapon, life, maxLife):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.life = life
        self.maxLife = maxLife
        self.charge = 0
        self.needed_charge = 0
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getLife(self):
        return self.life
    def setLife(self, life):
        self.life = life
    def getMaxLife(self):
        return self.maxLife
    def setMaxLife(self, maxLife):
        self.maxLife = maxLife
    def setArmor(self, armor):
        self.armor = armor
    def setWeapon(self, weapon):
        self.weapon = weapon    
    def getCharge(self):
        return self.charge
    def increaseCharge(self, qtd):
        self.charge += qtd
    def spendCharge(self, qtd):
        self.charge -= qtd
    def getDamage(self, target):
        if type(self.weapon.ATK) == list:
            dam1 = self.weapon.ATK[0]
            dam2 = self.weapon.ATK[1]
            charge = random.randint(dam1, dam2) 
            damage = charge - target.getDefense()
        else:
            charge = self.weapon.ATK 
            damage = charge - target.getDefense()
        target.takeDamage(damage)
        self.increaseCharge(charge)
        print('')
        print(f'{target.getName()} tomou {damage} de dano')
        print('')
        os.system('pause')
    def getUlt(self):
        pass
    def getDefense(self):
        def1 = self.armor.DEF[0]
        def2 = self.armor.DEF[1]
        defense = random.randint(def1, def2)
        return defense
    def takeDamage(self, dam):
        self.life -= dam
    def recover(self, hp):
        self.life += hp
        if self.life > self.maxLife:
            self.life = self.maxLife


class Paladin(Char):
    def __init__(self, name, armor, weapon, life, maxLife):
        super().__init__(name, armor, weapon, life, maxLife)
        self.weapon_type = 'axe'
        self.needed_charge = 40
    def getUlt(self, target):
        charge = self.weapon.ATK[0]
        damage = charge
        heal = self.weapon.ATK[1] - random.randint(2, 4)
        target.takeDamage(damage)
        self.recover(heal)
        self.spendCharge(40)
        print('')
        print(f'{target.getName()} tomou {damage} de dano')
        print('')
        print(f'{self.getName()} recuperou {heal} de vida')
        print('')
        os.system('pause')        
        

class Ranger(Char):
    def __init__(self, name, armor, weapon, life, maxLife):
        super().__init__(name, armor, weapon, life, maxLife)
        self.weapon_type = 'bow'
        self.needed_charge = 30
    def getUlt(self, target):
        charge = self.weapon.ATK * 2
        damage = charge - target.getDefense()
        target.takeDamage(damage)
        self.spendCharge(30)
        print('')
        print(f'{target.getName()} tomou {damage} de dano')
        print('')
        os.system('pause')


class Druid(Char):
    def __init__(self, name, armor, weapon, life, maxLife):
        super().__init__(name, armor, weapon, life, maxLife)
        self.weapon_type = 'spear'
        self.needed_charge = 22
    def getUlt(self, target):
        hits = random.randint(2,4)
        charge = self.weapon.ATK[0] * hits
        damage = charge
        target.takeDamage(damage)
        self.spendCharge(30)
        print('')
        print(f'{target.getName()} foi acertado {hits} vezes e tomou {damage} de dano')
        print('')
        os.system('pause')

npc1 = Paladin('Paladino Renegado', starterArmor, starterAxe, 100, 100)
npc2 = Druid('Druida Traidor', starterArmor, starterSpear, 100, 100)
npc3 = Ranger('Ladrão Arqueiro', starterArmor, starterBow, 100, 100)