from monster import *
from loot import *
loot = {
    "weapon": {
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
    },
    
"armor": {
        "leather armor": {"gold-value": 5, "armor": 6},
        "hide armor": {"gold-value": 15, "armor": 5},
        "studded leather armor": {"gold-value": 25, "armor": 7},
        "breastplate armor": {"gold-value": 45, "armor": 9},
        "half plate": {"gold-value": 200, "armor": 10},
        "splint armor": {"gold-value": 150, "armor": 12},
        "full plate armor": {"gold-value": 600, "armor": 15},
        "shield": {"gold-value": 12, "armor": 2},
    
        "magic leather armor": {"gold-value": 5 * 4, "armor": 6, "magic-armor-bonus": 3},
        "magic hide armor": {"gold-value": 15 * 4, "armor": 5,"magic-armor-bonus": 2},
        "magic studded leather armor": {"gold-value": 25 * 4, "armor": 7,"magic-armor-bonus": 5},
        "magic breastplate armor": {"gold-value": 45 * 4, "armor": 9,"magic-armor-bonus": 6},
        "magic half plate": {"gold-value": 200 * 4, "armor": 10,"magic-armor-bonus": 9},
        "magic splint armor": {"gold-value": 150 * 4, "armor": 12,"magic-armor-bonus": 10},
        "magic full plate armor": {"gold-value": 600 * 4, "armor": 15,"magic-armor-bonus": 12},
        "magic shield": {"gold-value": 12 * 4, "armor": 18,"magic-armor-bonus": 16}
    },

"misc":{
    "rags": {"gold-value": 0.01},
    "bones": {"gold-value": 0.04},
    "scrap leather": {"gold-value": 2},
    "gold coin": {"value": random.randint(1,25)},
    "gold ingot": {"gold-value": 10},
    "gold ore": {"gold-value": 6},
    "pure gold ore": {"gold-value": 12},
    "goddess tears": {"gold-value": 300}

},


"potions": {
    "lesser healing": {"health": 4, "value": 10},
    "greater healing": {"health": 10, "value": 50},
    "lesser strengthening": {"attack": 4, "value": 40},
    "greater strengthening": {"attack": 10, "value": 90},
    "lesser resistence": {"defense": 4, "value": 30},
    "greater resistence": {"defense": 10, "value": 100}
}
}

class Player:
    def __init__(self, health, attack, defense):
        self.name = ""
        self.health = health
        self.base_attack = attack
        self.attack = attack
        self.defense = defense
        self.max_health = health
        self.gold = 0
        self.inventory_limit = 8
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
        total_items_added = 0
        
        for loot_type, items in loot.items():
            if loot_type not in self.inventory:
                self.inventory[loot_type] = []
            for item in items:
                if len(self.inventory['weapons']) + len(self.inventory['armor']) + len(self.inventory['shields']) + len(self.inventory['potions']) + len(self.inventory['misc']) >= 8:
                    print("Inventory full. Cannot pick up more items.")
                    return
                
                if loot_type == 'misc' and 'gold piece' in item[1]: 
                    gold_value = loot_misc["gold coin"]["value"]
                    self.gold += gold_value
                    print(f"Added {gold_value} gold to your total.")
                else:
                    self.inventory[loot_type].append(item)
                    total_items_added += 1

        if total_items_added > 0:
            print(f"Added {total_items_added} items to your inventory.")
        else:
            print("No items were added to your inventory.")


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
        if loot_type in self.inventory and 0 <= item_index < len(self.inventory[loot_type]):
            item = self.inventory[loot_type].pop(item_index)
            item_name, item_stats = item
            gold_value = item_stats.get("gold-value", 0)
            self.gold += gold_value
            print(f"Sold {item_name} for {gold_value} gold. Your new gold amount is {self.gold}.")
        else:
            print("Invalid item or item index.")


    def get_sellable_items(self):
        sellable_items = []
        for category, items in self.inventory.items():
            for i, (item_name, item_stats) in enumerate(items):
                sellable_items.append((category, i, item_name, item_stats))
        return sellable_items

    def format_item(self, loot_type, item):
        item_name, item_stats = item
        stats = ", ".join([f"{k}: {v}" for k, v in item_stats.items()])
        return f"{item_name} - {stats}"


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

    def add_item_to_inventory(self, item_name, item_stats, category):
        if category in self.inventory:
            if len(self.inventory[category]) < 8:  
                self.inventory[category].append((item_name, item_stats))
            else:
                print("Inventory is full.")
        else:
            print("Invalid category.")