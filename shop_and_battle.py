def shop(player):
    shop_weapons = {
        "dagger": {"gold-value": 2, "damage": 2, "magic-damage-bonus": 1},
        "shortsword": {"gold-value": 5, "damage": 4, "magic-damage-bonus": 2},
        "longsword": {"gold-value": 10, "damage": 6, "magic-damage-bonus": 3},
        "shortbow": {"gold-value": 4, "damage": 5, "magic-damage-bonus": 5},
        "longbow": {"gold-value": 8, "damage": 10, "magic-damage-bonus": 9},
        "hand crossbow": {"gold-value": 6, "damage": 7, "magic-damage-bonus": 9},
        "light crossbow": {"gold-value": 8, "damage": 10, "magic-damage-bonus": 12},
        "heavy crossbow": {"gold-value": 12, "damage": 14, "magic-damage-bonus": 16},
    }
    
    shop_armor = {
        "leather armor": {"gold-value": 5, "armor": 6},
        "hide armor": {"gold-value": 4, "armor": 5},
        "studded leather armor": {"gold-value": 7, "armor": 7},
        "breastplate armor": {"gold-value": 6, "armor": 9},
        "half plate": {"gold-value": 8, "armor": 10},
        "splint armor": {"gold-value": 10, "armor": 12},
        "full plate armor": {"gold-value": 12, "armor": 15},
        "shield": {"gold-value": 12, "armor": 18},
    }
    
    print("Welcome to the shop! Here are the items available for purchase:")
    
    print("\nWeapons:")
    for i, (item_name, item_stats) in enumerate(shop_weapons.items()):
        print(f"{i}: {item_name} (worth {item_stats['gold-value']} gold)")

    print("\nArmors:")
    for i, (item_name, item_stats) in enumerate(shop_armor.items()):
        print(f"{i + len(shop_weapons)}: {item_name} (worth {item_stats['gold-value']} gold)")

    print("Enter the number of the item you want to buy, or type 'exit' to leave the shop:")
    choice = input()
    
    if choice.lower() == 'exit':
        print("Thank you for visiting the shop!")
        return
    
    try:
        index = int(choice)
        items = list(shop_weapons.items()) + list(shop_armor.items())
        if 0 <= index < len(items):
            item_name, item_stats = items[index]
            if player.gold >= item_stats['gold-value']:
                if item_name in shop_weapons:
                    player.inventory['weapons'].append((item_name, item_stats))
                else:
                    player.inventory['armor'].append((item_name, item_stats))
                player.gold -= item_stats['gold-value']
                print(f"Purchased {item_name} for {item_stats['gold-value']} gold.")
            else:
                print("You don't have enough gold.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def battle(player, monster):
    while player.health > 0 and monster.health > 0:
        monster.health -= player.attack
        if monster.health <= 0:
            loot = monster.drop_loot()
            return f"You have bested the {monster.name} in combat!", loot
        
        player.health -= max(0, monster.attack - player.defense)
        if player.health <= 0:
            return "You have been defeated by the monster.", None
    
    if player.defense > monster.attack:
        loot = monster.drop_loot()
        return f"The monster drops its weapon and runs away! It dropped: {player.format_item('weapons', loot['weapons'][0])}", loot
    
    loot = monster.drop_loot()
    return f"You have bested the {monster.name} in combat!", loot