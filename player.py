from monster import *
from random import choice
from loot import *
class Player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.max_health = self.health
        self.inventory = {"weapons": [], "armor": [], "shields": [], "misc": []}
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_shield = None
        self.total_gold = 0

    def get_attack_stat(self):
        return self.attack
    
    def get_defense_stat(self):
        return self.defense

    def deal_damage_monster(self, monster):
        damage = self.attack - monster.defense
        if damage > 0:
            monster.health -= damage

    def get_total_gold(self):
        return self.total_gold

    def format_item(self, loot_type, item):
        item_name, item_stats = item
        stats = ", ".join([f"{k}: {v}" for k, v in item_stats.items()])
        return f"{item_name}: {stats}\n"

    def pick_up_loot(self, loot):
        for loot_type, items in loot.items():
            for item in items:
                if len(self.inventory[loot_type]) < 8:
                    self.inventory[loot_type].append(item)
                else:
                    print(f"Cannot add more items to {loot_type}. Inventory full.")
                    break

    def equip_weapon(self, index):
        weapon = self.inventory['weapons'][index]
        self.equipped_weapon = weapon
        self.attack += weapon[1]['damage']
        print(f"Equipped {weapon[0]}")

    def equip_armor(self, index):
        armor = self.inventory['armor'][index]
        self.equipped_armor = armor
        self.defense += armor[1]['armor']
        print(f"Equipped {armor[0]}")

    def equip_shield(self, index):
        shield = self.inventory['shields'][index]
        self.equipped_shield = shield
        self.defense += shield[1]['armor']
        print(f"Equipped {shield[0]}")

    def get_sellable_items(self):
        sellable_items = []
        for loot_type, items in self.inventory.items():
            for i, item in enumerate(items):
                sellable_items.append((loot_type, i, item))
        return sellable_items

    def sell_item(self, loot_type, index):
        if loot_type in self.inventory and 0 <= index < len(self.inventory[loot_type]):
            item = self.inventory[loot_type].pop(index)
            gold_value = item[1].get("gold-value", 0)  
            self.total_gold += gold_value 
            print(f"You sold {item[0]} for {gold_value} gold.")
        else:
            print("Invalid item index or item type.")

    def rest(self):
        self.health = self.max_health
        print("Restored health to full.")

    def display_gold(self):
        print(f"You have {self.total_gold} gold.")