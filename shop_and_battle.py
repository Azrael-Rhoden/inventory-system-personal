from player import *
def shop(hero):
    shop_weapons = {
        "dagger": {"gold-value": 2, "damage": 2, "magic-damage-bonus": 1},
        "shortsword": {"gold-value": 5, "damage": 4, "magic-damage-bonus": 2},
        "longsword": {"gold-value": 10, "damage": 6, "magic-damage-bonus": 3},
        "shortbow": {"gold-value": 4, "damage": 5, "magic-damage-bonus": 5},
        "longbow": {"gold-value": 8, "damage": 10, "magic-damage-bonus": 9},
        "hand crossbow": {"gold-value": 6, "damage": 7, "magic-damage-bonus": 9},
        "light crossbow": {"gold-value": 8, "damage": 10, "magic-damage-bonus": 12},
        "heavy crossbow": {"gold-value": 12, "damage": 14, "magic-damage-bonus": 16}
    }

    shop_armor = {
        "leather armor": {"gold-value": 5, "armor": 6},
        "hide armor": {"gold-value": 4, "armor": 5},
        "studded leather armor": {"gold-value": 7, "armor": 7},
        "breastplate armor": {"gold-value": 6, "armor": 9},
        "half plate": {"gold-value": 8, "armor": 10},
        "splint armor": {"gold-value": 10, "armor": 12},
        "full plate armor": {"gold-value": 12, "armor": 15},
        "shield": {"gold-value": 12, "armor": 18}
    }

    while True:
        print("Welcome to the shop! Would you like to buy or sell items? enter show gold to see how much gold you have. (buy/sell/exit)")
        action = input().lower()
        if action == "show gold":
            hero.display_gold()
            continue
        if action == "buy":
            print("What would you like to buy? (weapons/armor)")
            category = input().lower()
            
            if category == "weapons":
                print("Available weapons:")
                for i, (item_name, item_stats) in enumerate(shop_weapons.items()):
                    print(f"{i}: {item_name} (worth {item_stats['gold-value']} gold)")
                try:
                    item_index = int(input("Enter the number of the weapon you want to buy: "))
                    if 0 <= item_index < len(shop_weapons):
                        item_name = list(shop_weapons.keys())[item_index]
                        item_stats = shop_weapons[item_name]
                        if hero.get_total_gold() >= item_stats["gold-value"]:
                            hero.inventory['weapons'].append((item_name, item_stats))
                            hero.total_gold -= item_stats["gold-value"]
                            print(f"You bought a {item_name}!")
                        else:
                            print("You do not have enough gold.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            elif category == "armor":
                print("Available armors:")
                for i, (item_name, item_stats) in enumerate(shop_armor.items()):
                    print(f"{i}: {item_name} (worth {item_stats['gold-value']} gold)")
                try:
                    item_index = int(input("Enter the number of the armor you want to buy: "))
                    if 0 <= item_index < len(shop_armor):
                        item_name = list(shop_armor.keys())[item_index]
                        item_stats = shop_armor[item_name]
                        if hero.get_total_gold() >= item_stats["gold-value"]:
                            hero.inventory['armor'].append((item_name, item_stats))
                            hero.total_gold -= item_stats["gold-value"]
                            print(f"You bought a {item_name}!")
                        else:
                            print("You do not have enough gold.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            else:
                print("Invalid category. Please choose 'weapons' or 'armor'.")
                
        elif action == "sell":
            sellable_items = hero.get_sellable_items()
            if not sellable_items:
                print("You have no items to sell.")
                continue

            print("Items you can sell:")
            for i, (loot_type, item_index, item) in enumerate(sellable_items):
                item_name, item_stats = item
                gold_value = item_stats.get("gold-value", 0)
                print(f"{i}: {item_name} (worth {gold_value} gold)")

            try:
                item_index = int(input("Enter the number of the item you want to sell: "))
                if 0 <= item_index < len(sellable_items):
                    loot_type, item_index, item = sellable_items[item_index]
                    hero.sell_item(loot_type, item_index)
                    print(f"You sold the {item[0]}!")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif action == "exit":
            break
        
        else:
            print("Invalid option. Please choose 'buy', 'sell', or 'exit'.")

            
def battle(player, monster):
    while player.health > 0 and monster.health > 0:
        monster.health -= player.attack
        if monster.health <= 0:
            loot = monster.drop_loot()
            return f"You have bested the {monster.name} in combat!",loot
        
        player.health -= max(0, monster.attack - player.defense)
        if player.health <= 0:
            return f"You have been defeated by the {monster.name}.", None
    
    if player.defense > monster.attack:
        loot = monster.drop_loot()
        return f"The monster drops its weapon and runs away! It dropped: {player.format_item('weapons', loot['weapons'][0])}", loot
    
    loot = monster.drop_loot()
    return f"You have bested the {monster.name} in combat!", loot