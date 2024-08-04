from monster import *
from random import choice
from loot import *
class Player:
    def __init__(self, health, attack, defense):
        self.name = ""
        self.health = health
        self.base_attack = attack
        self.attack = attack
        self.defense = defense
        self.max_health = health
        self.gold = 0
        self.inventory = {
            "weapons": [("Stick", {"attack": 2, "value": 1})],
            "armor": [],
            "shields": [],
            "potions": [],
            "misc": []
        }
        self.equipped_weapon = ("Stick", {"attack": 2, "value": 1})
        self.equipped_armor = None
        self.equipped_shield = None
    def update_attack_defense(self):
        self.attack = self.base_attack + (self.equipped_weapon[1]["attack"] if self.equipped_weapon else 0)
        self.defense = self.defense + (self.equipped_armor[1]["defense"] if self.equipped_armor else 0) + (self.equipped_shield[1]["defense"] if self.equipped_shield else 0)

    def total_inventory_count(self):
        return sum(len(items) for items in self.inventory.values())

    def get_attack_stat(self):
        return self.attack
    
    def get_defense_stat(self):
        return self.defense

    def deal_damage_monster(self, monster):
        damage = self.attack - monster.defense
        if damage > 0:
            monster.health -= damage

    def display_gold(self):
        print(f"You have {self.gold} gold.")

    def pick_up_loot(self, loot):
        for loot_type, items in loot.items():
            for item in items:
                if self.total_inventory_count() < 8:
                    self.inventory[loot_type].append(item)
                else:
                    print("Cannot add more items. Inventory full.")
                    return

    def display_inventory(self):
        print("Your inventory:")
        for loot_type, items in self.inventory.items():
            if items:
                print(f"{loot_type.capitalize()}:")
                for item in items:
                    print(f"  - {self.format_item(loot_type, item)}")
            else:
                print(f"No {loot_type}")
                

    def equip_weapon(self, index):
        weapons = self.inventory['weapons']
        if 0 <= index < len(weapons):
            self.equipped_weapon = weapons[index]
            print(f"Equipped weapon: {self.equipped_weapon}")
        else:
            print("Invalid weapon index.")

    def equip_armor(self, index):
        armors = self.inventory['armor']
        if 0 <= index < len(armors):
            self.equipped_armor = armors[index]
            print(f"Equipped armor: {self.equipped_armor}")
        else:
            print("Invalid armor index.")

    def equip_shield(self, index):
        shields = self.inventory['shields']
        if 0 <= index < len(shields):
            self.equipped_shield = shields[index]
            print(f"Equipped shield: {self.equipped_shield}")
        else:
            print("Invalid shield index.")

    def get_total_gold(self):
        return self.gold

    def sell_item(self, loot_type, item_index):
        item = self.inventory[loot_type].pop(item_index)
        item_name, item_stats = item  
        gold_value = item_stats.get("value", 0)
        self.gold += gold_value
        print(f"You have sold {item_name} for {gold_value} gold.")


    def get_sellable_items(self):
        sellable_items = []
        for loot_type, items in self.inventory.items():
            if loot_type != 'misc':
                for i, item in enumerate(items):
                    sellable_items.append((loot_type, item))
        return sellable_items

    def format_item(self, loot_type, item):
        if isinstance(item, dict):
            stats = ", ".join([f"{k}: {v}" for k, v in item.items()])
            item_name = item.get('name', 'Item')
            return f"{item_name} ({stats})"
        elif isinstance(item, tuple):
            item_name, item_stats = item
            stats = ", ".join([f"{k}: {v}" for k, v in item_stats.items()])
            return f"{item_name} ({stats})"
        else:
            return str(item)


    def drink_potion(self, index):
        potions = self.inventory['potions']
        if 0 <= index < len(potions):
            potion = potions.pop(index)
            self.health += potion.get("health", 0)
            self.attack += potion.get("attack", 0)
            self.defense += potion.get("defense", 0)
            print(f"You used a {potion}.")
        else:
            print("Invalid potion index.")

    def rest(self):
        self.health = self.max_health
        print("You have rested and regained your health.")