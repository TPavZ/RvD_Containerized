from dinosaur import Dinosaur # need to make a list of the dinos we crate using the dino class.

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self): #void name of dino = Dinosaur(name, attack_power, health)
        compsognathus = Dinosaur("The Compsognathus Pack")#, 50) #swarm
        stygimoloch = Dinosaur("Stygimoloch")#, 50) #headbut
        spinosaurus = Dinosaur("Spinosaurus")#, 50) #bite
        self.dinosaurs.append(compsognathus)
        self.dinosaurs.append(stygimoloch)
        self.dinosaurs.append(spinosaurus)

#compsognathus = Dinosaur("Compsognathus Pack", 30, 50) #swarm
#stygimoloch = Dinosaur("stygimoloch", 45, 100) #headbut
#spinosaurus = Dinosaur("spinosaurus", 55, 100) #bite