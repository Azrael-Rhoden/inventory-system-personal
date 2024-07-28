from monster import *
from random import choice
from loot import *
class Player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = {"weapons": [], "armor": [], "shields": [], "misc": []}
        self.equipped_weapon = None
        self.equipped_armor = None
        self.equipped_shield = None
        self.gold = 0


    def deal_damage_monster(self, monster):
        damage = self.attack - monster.defense
        if damage > 0:
            monster.health -= damage

    def get_total_gold(self):
        return self.gold

    def format_item(self, loot_type, item):
        item_name, item_stats = item
        stats = ", ".join([f"{k}: {v}" for k, v in item_stats.items()])
        return f"{item_name} ({stats})"

    def pick_up_loot(self, loot):
        for loot_type, items in loot.items():
            if loot_type in self.inventory:
                for item in items:
                    self.inventory[loot_type].append(item)
        print("Loot added to inventory.")

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

    def sell_item(self, loot_type, index):
        
        if loot_type not in self.inventory:
            print(f"Invalid loot type: {loot_type}")
            return

        
        print(f"Current inventory for {loot_type}: {self.inventory[loot_type]}")

        
        if index < 0 or index >= len(self.inventory[loot_type]):
            print(f"Invalid index: {index}. Cannot sell item.")
            return

        
        item = self.inventory[loot_type].pop(index)
        item_name = item[0]
        item_value = item[1]["gold-value"]
        self.gold += item_value
        print(f"Sold {item_name} for {item_value} gold. You now have {self.gold} gold.")

    def get_sellable_items(self):
        sellable_items = []
        for loot_type, items in self.inventory.items():
            for item in items:
                if loot_type == "weapons" and item != self.equipped_weapon:
                    sellable_items.append((loot_type, item))
                elif loot_type == "armor" and item != self.equipped_armor:
                    sellable_items.append((loot_type, item))
                elif loot_type == "shields" and item != self.equipped_shield:
                    sellable_items.append((loot_type, item))
                elif loot_type == "misc":
                    sellable_items.append((loot_type, item))
        return sellable_items

    def rest(self):
        self.health = 100
        print("Restored health to full.")