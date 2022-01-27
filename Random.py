# workingish battlefield

#from fleet import Fleet
#from herd import Herd
#from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()   
        self.herd = Herd()

    def run_game(self):
        start_game = self.display_welcome()
        if start_game == True:
            print("\nLets get ready to RUMBLE!!!\nRobots have been granted first attack.\n") 
            self.battle()
        else:
            self.run_game()

    def display_welcome(self):
        print("\n***WELCOME TO THE BATTLEFIELD***\n\n\t\tRobots\n\tVs.\n\t\tDinosaurs\n")
        new_game = input("Start A New Game? Yes or No: ").lower()
        if new_game == "yes":
            return True
        else:
            return False

    def battle(self): 
        self.herd.create_herd()
        self.fleet.create_fleet()
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0: 
            self.robo_turn()
            if len(self.herd.dinosaurs) > 0:         
                self.dino_turn()
        self.display_winners()
            
    def dino_turn(self): 
        print("The avaliable attackers: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack with. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} Has been selected to make an attack.")
        print("\nAvailable robot opponents to attack: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} attacks {self.fleet.robots[robo_selection].name}\n")
        print(f"{self.herd.dinosaurs[dino_selection].name}'s {self.herd.dinosaurs[dino_selection].attack_type[robo_selection]} does {self.herd.dinosaurs[dino_selection].attack_power[dino_selection]} damage to {self.fleet.robots[robo_selection].name}\n")
        print(f"\n{self.fleet.robots[robo_selection].name} has {(self.fleet.robots[robo_selection].health[robo_selection] - self.herd.dinosaurs[dino_selection].attack_power[dino_selection])} health remaining.")
        self.herd.dinosaurs[dino_selection].dino_attack(self.fleet.robots[robo_selection])
        if self.fleet.robots[robo_selection].health[robo_selection] <= 0:
            self.fleet.robots.remove(self.fleet.robots[robo_selection])

#did not work
        print(f"\n{self.herd.dinosaurs[dino_selection].name} attacks {self.fleet.robots[robo_selection].name}\n")
        print(f"{self.herd.dinosaurs[dino_selection].name}'s {self.herd.dinosaurs[dino_selection].attack_type[robo_selection]} does {self.herd.dinosaurs[dino_selection].attack_power[dino_selection]} damage to {self.fleet.robots[robo_selection].name}\n")
        
        if self.fleet.robots[robo_selection].health[robo_selection] >= 0:
            print(f"\n{self.fleet.robots[robo_selection].name} has {(self.fleet.robots[robo_selection].health[robo_selection] - self.herd.dinosaurs[dino_selection].attack_power[dino_selection])} health remaining.")
        self.herd.dinosaurs[dino_selection].dino_attack(self.fleet.robots[robo_selection])
        if self.fleet.robots[robo_selection].health[robo_selection] < 0:
            self.fleet.robots.remove(self.fleet.robots[robo_selection])
            print(f"\n{self.fleet.robots[robo_selection].name} has been ELIMINATED!")
#***********

            
    def robo_turn(self):
        print("Here are your avaliable attackers: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack with. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} Has been selected to make an attack")
        print("\nAvailable dinosaur opponents to attack: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} attacks {self.herd.dinosaurs[dino_selection].name}\n")
        print(f"{self.fleet.robots[robo_selection].name}'s {self.fleet.robots[robo_selection].weapon.wn[robo_selection]} does {self.fleet.robots[robo_selection].weapon.wap[robo_selection]} damage to {self.herd.dinosaurs[dino_selection].name}\n")
        print(f"\n{self.herd.dinosaurs[dino_selection].name} has {(self.herd.dinosaurs[dino_selection].health[dino_selection] - self.fleet.robots[robo_selection].weapon.wap[robo_selection])} health remaining.")
        self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        if self.herd.dinosaurs[dino_selection].health[dino_selection] <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_selection])

#did not work
        print(f"\n{self.fleet.robots[robo_selection].name} attacks {self.herd.dinosaurs[dino_selection].name}\n")
        print(f"{self.fleet.robots[robo_selection].name}'s {self.fleet.robots[robo_selection].weapon.wn[robo_selection]} does {self.fleet.robots[robo_selection].weapon.wap[robo_selection]} damage to {self.herd.dinosaurs[dino_selection].name}\n")
        self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        if self.herd.dinosaurs[dino_selection].health[dino_selection] > 0:
            print(f"\n{self.herd.dinosaurs[dino_selection].name} has {(self.herd.dinosaurs[dino_selection].health[dino_selection] - self.fleet.robots[robo_selection].weapon.wap[robo_selection])} health remaining.")
            self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        if self.herd.dinosaurs[dino_selection].health[dino_selection] <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_selection])
            print(f"\n{self.herd.dinosaurs[dino_selection].name} has been ELIMINATED!")  
#***********


    def show_doo(self): 
        index = 0
        for dino in self.herd.dinosaurs:
            print(f"{index} - {dino.name} - Attack Type & Power: {dino.attack_type[index]}, {dino.attack_power[index]} - Remaining Health: {dino.health[index]}")
            index += 1

    def show_roo(self): 
        index = 0
        for bot in self.fleet.robots:
            print(f"{index} - {bot.name} - Attack Weapon & Power: {bot.weapon.wn[index]}, {bot.weapon.wap[index]} - Remaining Health: {bot.health[index]}")
            index += 1      

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("Battle Champions Are The Robots!")
        elif len(self.fleet.robots) == 0:
            print("Battle Champions Are The Dinosaurs!")


#*****************************************************************
#MOST UP TO DATE WORKING

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()   
        self.herd = Herd()

    def run_game(self):
        start_game = self.display_welcome()
        if start_game == True:
            print("\nLets get ready to RUMBLE!!!\nRobots have been granted first attack.\n")
            print(input("Press enter to continue: ")) 
            self.battle()
        else:
            self.run_game()

    def display_welcome(self):
        print("\n***WELCOME TO THE BATTLEFIELD***\n\n\t\tRobots\n\tVs.\n\t\tDinosaurs\n")
        new_game = input("Start A New Game? Yes or No: ").lower()
        if new_game == "yes":
            return True
        else:
            return False

    def battle(self): 
        self.herd.create_herd()
        self.fleet.create_fleet()
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0: 
            self.robo_turn()
            if len(self.herd.dinosaurs) > 0:         
                self.dino_turn()
        self.display_winners()
        print(input("Press enter to continue: "))
        self.run_game()
            
    def dino_turn(self): 
        print("The avaliable attackers: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack with. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} Has been selected to make an attack.\n")
        print(input("Press enter to continue: "))
        print("\nAvailable robot opponents to attack: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} attacks {self.fleet.robots[robo_selection].name}\n")
        print(f"{self.herd.dinosaurs[dino_selection].name}'s {self.herd.dinosaurs[dino_selection].attack_type[robo_selection]} does {self.herd.dinosaurs[dino_selection].attack_power[dino_selection]} damage to {self.fleet.robots[robo_selection].name}\n")
        new_health = (self.fleet.robots[robo_selection].health[robo_selection] - self.herd.dinosaurs[dino_selection].attack_power[dino_selection])
        print(f"\n{self.fleet.robots[robo_selection].name} has {int(new_health)} health remaining.\n")
        print(input("Press enter to continue: "))
        self.herd.dinosaurs[dino_selection].dino_attack(self.fleet.robots[robo_selection])
        self.fleet.robots[robo_selection].health[robo_selection] = int(new_health)
        if self.fleet.robots[robo_selection].health[robo_selection] <= 0:
            self.fleet.robots.remove(self.fleet.robots[robo_selection])
            
    def robo_turn(self):
        print("Here are your avaliable attackers: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack with. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} Has been selected to make an attack\n")
        print(input("Press enter to continue: "))
        print("\nAvailable dinosaur opponents to attack: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} attacks {self.herd.dinosaurs[dino_selection].name}\n")
        print(f"{self.fleet.robots[robo_selection].name}'s {self.fleet.robots[robo_selection].weapon.wn[robo_selection]} does {self.fleet.robots[robo_selection].weapon.wap[robo_selection]} damage to {self.herd.dinosaurs[dino_selection].name}\n")
        new_health = (self.herd.dinosaurs[dino_selection].health[dino_selection] - self.fleet.robots[robo_selection].weapon.wap[robo_selection])
        print(f"\n{self.herd.dinosaurs[dino_selection].name} has {int(new_health)} health remaining.\n")
        print(input("Press enter to continue: "))
        self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        self.herd.dinosaurs[dino_selection].health[dino_selection] = int(new_health)
        if self.herd.dinosaurs[dino_selection].health[dino_selection] <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_selection])
        
    def show_doo(self): 
        index = 0
        for dino in self.herd.dinosaurs:
            print(f"{index} - {dino.name} - Attack Type & Power: {dino.attack_type[index]}, {dino.attack_power[index]} - Remaining Health: {dino.health[index]}")
            index += 1

    def show_roo(self): 
        index = 0
        for bot in self.fleet.robots:
            print(f"{index} - {bot.name} - Attack Weapon & Power: {bot.weapon.wn[index]}, {bot.weapon.wap[index]} - Remaining Health: {bot.health[index]}")
            index += 1      

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("\nALL Dinosaurs Have Been Eliminated!")
            print("Battle Champions Are The Robots!\n\n")
        elif len(self.fleet.robots) == 0:
            print("\n ALL Robots Have Been Eliminated!")
            print("Battle Champions Are The Dinosaurs!\n\n")
            

#more turns that did not work.
def dino_turn(self): 
        print("The avaliable attackers: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack with. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} Has been selected to make an attack.\n")
        print(input("Press enter to continue: "))
        print("Available robot opponents to attack: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack. [0, 1, or 2]: "))
        print(f"\n{self.herd.dinosaurs[dino_selection].name} attacks {self.fleet.robots[robo_selection].name}\n")
        print(f"{self.herd.dinosaurs[dino_selection].name}'s {self.herd.dinosaurs[dino_selection].attack_type[robo_selection]} does {self.herd.dinosaurs[dino_selection].attack_power[dino_selection]} damage to {self.fleet.robots[robo_selection].name}\n")
        new_health = (self.fleet.robots[robo_selection].health[robo_selection] - self.herd.dinosaurs[dino_selection].attack_power[dino_selection])
        self.fleet.robots[robo_selection].health[robo_selection] = int(new_health)
        if new_health > 0:
            print(f"{self.fleet.robots[robo_selection].name} has {int(new_health)} health remaining.\n")
            print(input("Press enter to continue: "))
        self.herd.dinosaurs[dino_selection].dino_attack(self.fleet.robots[robo_selection])
        if self.fleet.robots[robo_selection].health[robo_selection] <= 0:
            self.fleet.robots.remove(self.fleet.robots[robo_selection])
            print(f"{self.fleet.robots[robo_selection].name} Has been eliminated.")
            
def robo_turn(self):
        print("Here are your avaliable attackers: ")
        self.show_roo()
        robo_selection = int(input("\nChoose a Robot to attack with. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} Has been selected to make an attack\n")
        print(input("Press enter to continue: "))
        print("Available dinosaur opponents to attack: ")
        self.show_doo()
        dino_selection = int(input("\nChoose a Dinosaur to attack. [0, 1, or 2]: "))
        print(f"\n{self.fleet.robots[robo_selection].name} attacks {self.herd.dinosaurs[dino_selection].name}\n")
        print(f"{self.fleet.robots[robo_selection].name}'s {self.fleet.robots[robo_selection].weapon.wn[robo_selection]} does {self.fleet.robots[robo_selection].weapon.wap[robo_selection]} damage to {self.herd.dinosaurs[dino_selection].name}\n")
        new_health = (self.herd.dinosaurs[dino_selection].health[dino_selection] - self.fleet.robots[robo_selection].weapon.wap[robo_selection])
        self.herd.dinosaurs[dino_selection].health[dino_selection] = int(new_health)
        if new_health > 0:
            print(f"{self.herd.dinosaurs[dino_selection].name} has {int(new_health)} health remaining.\n")
            print(input("Press enter to continue: "))
        self.fleet.robots[robo_selection].bot_attack(self.herd.dinosaurs[dino_selection])
        if self.herd.dinosaurs[dino_selection].health[dino_selection] <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_selection])
            print(f"{self.herd.dinosaurs[dino_selection].name} Has been eliminated.")