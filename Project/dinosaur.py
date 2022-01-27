class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = [30, 45, 55]
        self.attack_type = ["Swarm", "Headbutt", "Bite"]
        self.health = [50, 100, 100]

    def dino_attack(self, robot): #void
        index = 0
        robot.health[index] -= self.attack_power[index] 
        return robot.health[index]
        
        #this makes is what makes  sense to me will it work? not sure.