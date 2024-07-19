import random
from loot import *
monster_dict = {
                        "easy": {
                            "green slime": {"health": 2, "attack": 1, "defense": 0},
                            "red slime": {"health": 1, "attack": 3, "defense": 2},
                            "blue slime": {"health": 3, "attack": 1, "defense": 1},
                            "gold slime": {"health": 5, "attack": 3, "defense": 3}}, 

                        "medium" : {
                            "goblin": {"health": 8, "attack": 3, "defense": 2},
                            "orc": {"health": 12,"attack": 9, "defense": 3},
                            "ogre": {"health": 15, "attack": 12, "defense": 5}
                            }, 

                        "hard": {
                            "hill giant": {"health": 17, "attack": 16, "defense": 8},
                            "red dragon": {"health": 25, "attack": 20, "defense": 10}},
                            "ancient red dragon": {"health": 30, "attack": 25, "defense": 13}
                            }
class Monster:
    def __init__(self):
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.name = ""
        self.difficulty = self.select_difficulty()

    def select_difficulty(self):
        while True:
            print("Please select your destination")
            print(" 1. EASY: Slime plains \n 2. MEDIUM: Mountain side \n 3. HARD: Giant plains and dragon cave")
            selection = input().lower()
            if selection == "easy":
                print("entering slime plains...")
                return "easy"
            elif selection == "medium":
                print("entering mountain side...")
                return "medium"
            elif selection == "hard":
                print("entering giant plains and dragon cave...")
                return "hard"
            else:
                print("Try again, not an accepted input")

    def create_monster(self):
        if self.difficulty == "easy":
            monster_name, monster_stats = random.choice(list(monster_dict["easy"].items()))
        elif self.difficulty == "medium":
            monster_name, monster_stats = random.choice(list(monster_dict["medium"].items()))
        elif self.difficulty == "hard":
            monster_name, monster_stats = random.choice(list(monster_dict["hard"].items()))
        else:
            raise ValueError("Invalid difficulty level")

        self.health = monster_stats["health"]
        self.attack = monster_stats["attack"]
        self.defense = monster_stats["defense"]
        self.name = monster_name

    def deal_damage_player(self, player):
        
        if self.attack > 0:
            player.health -= self.attack - player.defense

    