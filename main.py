import random
monster_dict = {"easy": {
                            "green slime": {"health": 2, "attack": 1, "defense": 0},
                            "red slime": {"health": 1, "attack": 3, "defense": 2},
                            "blue slime": {"health": 3, "attack": 1, "defense": 1},
                            "gold slime": {"health": 5, "attack": 3, "defense": 3}}, 

                             "medium" : {
                            "goblin": {"health": 4, "attack": 3, "defense": 2},
                            "orc": {"health": 6,"attack": 7, "defense": 3},
                            "ogre": {"health": 10, "attack": 7, "defense": 5}
                            }, 

                             "hard": {
                            "hill giant": {"health": 12, "attack": 9, "defense": 8},
                            "red dragon": {"health": 14, "attack": 10, "defense": 10}},
                            "ancient red dragon": {"health": 20, "attack": 15, "defense": 13}
                            }
class Monster:
    def __init__(self, health, attack, defense, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.name = name
        self.difficulty = select_difficulty()
    
    def create_monster(self):
        easy = self.monster_dict["easy"]
        medium = self.monster_dict["medium"]
        hard = self.monster_dict["hard"]

        if self.difficulty.lower() == easy:
            pass
        if self.difficulty.lower() == medium:
            pass
        if self.difficulty.lower() == hard:
            pass

    def assign_loot(self):
        pass


    def take_damage_monster(self):
        pass

    
class Player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.player_inventory = []
        self.gold_value = 0

    
    def add_to_inventory(self, item):
        pass

    def sell_item(self, item):
        pass

loot = [
        {"rags": 10},
        {"staff of the mundane": 100}, 
        {"sword of the flu": 200}, 
        {"stick of truth": 400},
        {"greatsword of fire": 600},
        {"bow of aim-bot": 1000},
        {"ark of value": 7000}
        ] 

def main():
    difficulty = select_difficulty()
    
    
def select_difficulty():
    while True:
        print("Please select your goal")
        print(" 1.EASY: Slime plains \n 2.MEDIUM: Mountain side \n 3.HARD giant plains and dragon cave")
        selection = input()
        if selection.lower() == "easy":
            return "You`ve selected the Slime plains"
            
        if selection.lower() == "medium":
            return "You`ve selected the mountain side"
            
        if selection.lower() == "hard":
            return "You`ve selected the giant plains and dragon caves"
            
        else :
            print("try again, not an accepted input")
        continue
    
main()