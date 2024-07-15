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
        easy = monster_dict["easy"]
        medium = monster_dict["medium"]
        hard = monster_dict["hard"]
        if self.difficulty == easy:
            for monster,value in random.choice(monster_dict):
                self.health = easy[monster][value]["health"]
                self.attack = easy[monster][value]["attack"]
                self.defense = easy[monster][value]["defense"]
                self.name = easy[monster]

        if self.difficulty == medium:
            for monster,value in random.choice(monster_dict):
                self.health = medium[monster][value]["health"]
                self.attack = medium[monster][value]["attack"]
                self.defense = medium[monster][value]["defense"]
                self.name = medium[monster]

        if self.difficulty == hard:
            for monster,value in random.choice(monster_dict):
                self.health = hard[monster][value]["health"]
                self.attack = hard[monster][value]["attack"]
                self.defense = hard[monster][value]["defense"]
                self.name = hard[monster]


    def deal_damage_player(self,other):
        other.health -= self.attack -  other.defense
    
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