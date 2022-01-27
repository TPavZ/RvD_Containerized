from robot import Robot # need to make a list of the bots we crate using the bot class.
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self): #void name of bots = Robot(name, health, weapon) and weapon from Weapon(name, power)
        wall_e = Robot("WALL-E")
        droideka = Robot("Droideka")
        c12 = Robot("C12")
        self.robots.append(wall_e)
        self.robots.append(droideka)
        self.robots.append(c12)