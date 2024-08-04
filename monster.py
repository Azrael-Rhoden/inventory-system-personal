import random
from loot import *
monster_dict = {
                        "easy": {
                            "green slime": {"health": 5, "attack": 1, "defense": 0},
                            "red slime": {"health": 7, "attack": 3, "defense": 2},
                            "blue slime": {"health": 6, "attack": 1, "defense": 1},
                            "gold slime": {"health": 9, "attack": 3, "defense": 3}}, 

                        "medium" : {
                            "goblin": {"health": 12, "attack": 3, "defense": 2},
                            "orc": {"health": 16,"attack": 9, "defense": 3},
                            "ogre": {"health": 23, "attack": 12, "defense": 5}
                            }, 

                        "hard": {
                            "hill giant": {"health": 30, "attack": 16, "defense": 8},
                            "red dragon": {"health": 45, "attack": 20, "defense": 10}},
                            "ancient red dragon": {"health": 50, "attack": 25, "defense": 13}
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
            print("Please select your destination\n")
            print(" 1. EASY: Slime plains \n 2. MEDIUM: Mountain side \n 3. HARD: Giant plains and dragon cave")
            selection = input().lower()
            if selection == "easy" or selection == "1":
                return "easy"
            elif selection == "medium" or selection == "2":
                return "medium"
            elif selection == "hard" or selection == "3":
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

        self.health = monster_stats["health"]
        self.attack = monster_stats["attack"]
        self.defense = monster_stats["defense"]
        self.name = monster_name
        print(f"A fearsome {self.name} emerges.")
        

    def drop_loot(self):
        equip = {
            'weapons': [],
            'armor': [],
            'shields': [],
            'potions': [],
            'misc': []
        }
        if self.difficulty == "easy":
            equip['misc'].append(("Gold Coin", {"gold-value": random.randint(1, 10)}))
        else:
            if random.random() < 0.5:
                equip['weapons'].append(("Sword", {"damage": 5, "gold-value": 100}))
            if random.random() < 0.5:
                equip['armor'].append(("Leather Armor", {"armor": 3, "gold-value": 75}))
            if random.random() < 0.5:
                equip['shields'].append(("Wooden Shield", {"armor": 2, "gold-value": 50}))
            if random.random() < 0.5:
                equip['potions'].append(("Lesser Healing Potion", {"health": 4, "gold-value": 10}))
            equip['misc'].append(("Gold Coin", {"gold-value": random.randint(1, 10)}))
        return equip