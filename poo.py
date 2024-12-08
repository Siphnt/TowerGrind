import random
import commun
"""orc = Monstre.__init__("orc")
orc.force

class Monstre(object):
    def __init__(self, type_monstre):
        self.bonus_force = 0
        if 'orc' in type_monstre:
            self.force = 15
            self.force_orc = 5
    
    def set_bonus_force(self, bonus):
        self.bonus_force = bonus
        
    def get_force(self):
        return self.force + random.randint(0,self.force_orc) + self.bonus_force
    
    force, agilité, constitution, mana"""

""" Entre 10 et 12 compris = 25 pv
    Entre 12 pas compris et 14 compris = 33 pv
    Entre 14 pas compris et 16 compris = 40 pv
    Entre 16 pas compris et 18 compris = 48 pv
    Entre 16 pas compris et 20 compris = 58 pv"""


    
class Orc(object):
    def __init__(self):
        self.force=random.randint(12,16)
        self.agilite=random.randint(5,12)
        self.constitution=random.randint(10,16)
        self.mana=0
        self.lvl=0
        if 10<=self.constitution<=12:
             self.vie=25
        if 12<self.constitution<=14:
            self.vie=33
        if 14<self.constitution<=16:
            self.vie=40
        if 16<self.constitution<=18:
            self.vie=48
        if 18<self.constitution<=20:
            self.vie=58
        if 20<self.constitution:
            self.vie=58
    def __repr__(self):
        return "force = "+str(self.force)+"\n"+ "agilite = "+ str(self.agilite)+"\n"+ "constitution  = "+str(self.constitution)+ "\n"+"mana = "+str(self.mana)+"\n"+"Vie = "+str(self.vie)+"\n"+"Lvl = "+str(self.lvl)
    
    def modif_stat(self):
        commun.modif_stat=(random.randint(0,15))
        if 5<=commun.modif_stat<=10: 
            self.force+=random.randint(0, 1)
            self.agilite+=random.randint(0, 1)
            self.constitution+=random.randint(0, 1)
    def get_lvl(self):
        if commun.raa==0:
            self.lvl=commun.lvl
            commun.raa=1
    def get_vie(self):
        if 10<=self.constitution<=12:
             self.vie=25
        if 12<self.constitution<=14:
            self.vie=33
        if 14<self.constitution<=16:
            self.vie=40
        if 16<self.constitution<=18:
            self.vie=48
        if 18<self.constitution<=20:
            self.vie=58
        if 20<self.constitution:
            self.vie=58+random.randint(1,self.lvl)
    """def degat(self):
        if self.vie==0:
            del self
    def test(self):"""
        
        
        
        