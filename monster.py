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
        print(f"Created monster: {self.name}")
        print(f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}")

    def drop_loot(self):
        loot_weapons = {
            "dagger": {"gold-value": 2, "damage": 2,  "magic-damage-bonus": 1},
            "shortsword": {"gold-value": 5, "damage": 4,  "magic-damage-bonus": 2},
            "longsword": {"gold-value": 10, "damage": 6,  "magic-damage-bonus": 3},
            "shortbow": {"gold-value": 4, "damage": 5,  "magic-damage-bonus": 5},
            "longbow": {"gold-value": 8, "damage": 10,  "magic-damage-bonus": 9},
            "hand crossbow": {"gold-value": 6, "damage": 7,  "magic-damage-bonus": 9},
            "light crossbow": {"gold-value": 8, "damage": 10,  "magic-damage-bonus": 12},
            "heavy crossbow": {"gold-value": 12, "damage": 14,  "magic-damage-bonus": 16},

            "magic dagger": {"gold-value": 2 * 4, "damage": 2, "magic-damage-bonus": 1},
            "magic shortsword": {"gold-value": 5 * 4, "damage": 4, "magic-damage-bonus": 2},
            "magic longsword": {"gold-value": 10 * 4, "damage": 6, "magic-damage-bonus": 3},
            "magic shortbow": {"gold-value": 4 * 4, "damage": 5, "magic-damage-bonus": 5},
            "magic longbow": {"gold-value": 8 * 4, "damage": 10, "magic-damage-bonus": 9},
            "magic hand crossbow": {"gold-value": 6 * 4, "damage": 7, "magic-damage-bonus": 9},
            "magic light crossbow": {"gold-value": 8 * 4, "damage": 10, "magic-damage-bonus": 12},
            "magic heavy crossbow": {"gold-value": 12 * 4, "damage": 14, "magic-damage-bonus": 16}
        }
        loot_armor = {
            "leather armor": {"gold-value": 5, "armor": 6},
            "hide armor": {"gold-value": 4, "armor": 5},
            "studded leather armor": {"gold-value": 7, "armor": 7},
            "breastplate armor": {"gold-value": 6, "armor": 9},
            "half plate": {"gold-value": 8, "armor": 10},
            "splint armor": {"gold-value": 10, "armor": 12},
            "full plate armor": {"gold-value": 12, "armor": 15},
            "magic leather armor": {"gold-value": 5 * 4, "armor": 6, "magic-armor-bonus": 3},
            "magic hide armor": {"gold-value": 4 * 4, "armor": 5,"magic-armor-bonus": 2},
            "magic studded leather armor": {"gold-value": 7 * 4, "armor": 7,"magic-armor-bonus": 5},
            "magic breastplate armor": {"gold-value": 6 * 4, "armor": 9,"magic-armor-bonus": 6},
            "magic half plate": {"gold-value": 8 * 4, "armor": 10,"magic-armor-bonus": 9},
            "magic splint armor": {"gold-value": 10 * 4, "armor": 12,"magic-armor-bonus": 10},
            "magic full plate armor": {"gold-value": 12 * 4, "armor": 15,"magic-armor-bonus": 12}
        }
        loot_misc = {
            "rags": {"gold-value": 0.01},
            "bones": {"gold-value": 0.04},
            "scrap leather": {"gold-value": 2},
            "gold piece": {"gold-value": 1},
            "gold ingot": {"gold-value": 10},
            "gold ore": {"gold-value": 6},
            "pure gold ore": {"gold-value": 12}
        }
        loot_shields = {
            "shield": {"gold-value": 12, "armor": 18},
            "magic shield": {"gold-value": 12 * 4, "armor": 18,"magic-armor-bonus": 16}
        }
        
        loot = {
            "weapons": [],
            "armor": [],
            "shields": [],
            "misc": []
        }
        
        if random.choice([True, False]):
            weapon = random.choice(list(loot_weapons.items()))
            loot["weapons"].append(weapon)
        
        if random.choice([True, False]):
            armor = random.choice(list(loot_armor.items()))
            loot["armor"].append(armor)
        
        if random.choice([True, False]):
            shield = random.choice(list(loot_shields.items()))
            loot["shields"].append(shield)
        
        if random.choice([True, False]):
            misc = random.choice(list(loot_misc.items()))
            loot["misc"].append(misc)
        
        return loot