from player import *
from main import *

def custom_input(prompt=""):
    user_input = input(prompt)
    if user_input.lower() == "exit":
        print("Exiting the game. Goodbye!")
        exit()
    return user_input

def shop(hero):
    shop_weapons = {
        "dagger": {"gold-value": 2, "damage": 2,  "magic-damage-bonus": 1},
        "shortsword": {"gold-value": 5, "damage": 4,  "magic-damage-bonus": 2},
        "longsword": {"gold-value": 10, "damage": 6,  "magic-damage-bonus": 3},
        "shortbow": {"gold-value": 4, "damage": 5,  "magic-damage-bonus": 5},
        "longbow": {"gold-value": 8, "damage": 10,  "magic-damage-bonus": 9},
        "hand crossbow": {"gold-value": 6, "damage": 7,  "magic-damage-bonus": 9},
        "light crossbow": {"gold-value": 8, "damage": 10,  "magic-damage-bonus": 12},
        "heavy crossbow": {"gold-value": 12, "damage": 14,  "magic-damage-bonus": 16},
    }
    shop_armor = {"leather armor": {"gold-value": 5, "armor": 6},
        "hide armor": {"gold-value": 15, "armor": 5},
        "studded leather armor": {"gold-value": 25, "armor": 7},
        "breastplate armor": {"gold-value": 45, "armor": 9},
        "half plate": {"gold-value": 200, "armor": 10},
        "splint armor": {"gold-value": 150, "armor": 12},
        "full plate armor": {"gold-value": 600, "armor": 15},
        }
    shop_shields = {"shield": {"gold-value": 12, "armor": 2},}
    shop_potions = {"lesser healing": {"health": 4, "value": 10},
    "greater healing": {"health": 10, "value": 50},
    "lesser strengthening": {"attack": 4, "value": 40},
    "greater strengthening": {"attack": 10, "value": 90},
    "lesser resistence": {"defense": 4, "value": 30},
    "greater resistence": {"defense": 10, "value": 100}}

    while True:
        print("Would you like to buy or sell items? (buy/sell/leave)")
        action = custom_input().lower()
        if action == "buy":
            print("Items available for purchase:")
            print("Weapons:")
            for i, (item_name, item_stats) in enumerate(shop_weapons.items()):
                print(f"{i}: {item_name} - {item_stats['gold-value']} gold")
            print("Armor:")
            for i, (item_name, item_stats) in enumerate(shop_armor.items()):
                print(f"{i + len(shop_weapons)}: {item_name} - {item_stats['gold-value']} gold")
            print("Shields:")
            for i, (item_name, item_stats) in enumerate(shop_shields.items()):
                print(f"{i + len(shop_weapons) + len(shop_armor)}: {item_name} - {item_stats['gold-value']} gold")
            print("Potions:")
            for i, (item_name, item_stats) in enumerate(shop_potions.items()):
                print(f"{i + len(shop_weapons) + len(shop_armor) + len(shop_shields)}: {item_name} - {item_stats['value']} gold")
            print("Which item would you like to buy? (enter the item number or type 'leave' to leave)")
            item_index = custom_input()
            if item_index.lower() == "leave":
                break
            try:
                item_index = int(item_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= item_index < len(shop_weapons):
                item_name, item_stats = list(shop_weapons.items())[item_index]
            elif len(shop_weapons) <= item_index < len(shop_weapons) + len(shop_armor):
                item_name, item_stats = list(shop_armor.items())[item_index - len(shop_weapons)]
            elif len(shop_weapons) + len(shop_armor) <= item_index < len(shop_weapons) + len(shop_armor) + len(shop_shields):
                item_name, item_stats = list(shop_shields.items())[item_index - len(shop_weapons) - len(shop_armor)]
            elif len(shop_weapons) + len(shop_armor) + len(shop_shields) <= item_index < len(shop_weapons) + len(shop_armor) + len(shop_shields) + len(shop_potions):
                item_name, item_stats = list(shop_potions.items())[item_index - len(shop_weapons) - len(shop_armor) - len(shop_shields)]
            else:
                print("Invalid item number.")
                continue

            if hero.gold >= item_stats.get("gold-value", item_stats.get("value", 0)):
                hero.gold -= item_stats.get("gold-value", item_stats.get("value", 0))
                hero.add_item_to_inventory(item_name, item_stats)
                print(f"You have purchased {item_name}!")
            else:
                print("You do not have enough gold to buy this item.")
        
        elif action == "sell":
            sellable_items = hero.get_sellable_items()
            if not sellable_items:
                print("You have no items to sell.")
                continue

            print("Items in your inventory:")
            for i, (loot_type, item) in enumerate(sellable_items):
                item_name, item_stats = item
                gold_value = item_stats.get("gold-value", item_stats.get("value", 0))
                print(f"{i}: {hero.format_item(loot_type, item)} (worth {gold_value} gold)")

            print("Which item would you like to sell? (enter the item number or type 'leave' to leave)")
            item_index = custom_input()
            if item_index.lower() == "leave":
                break
            try:
                item_index = int(item_index)
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= item_index < len(sellable_items):
                loot_type, item = sellable_items[item_index]
                hero.sell_item(loot_type, item_index)
                print("Item sold successfully.")
            else:
                print("Invalid item number.")
        
        elif action == "leave":
            print("Thank you for visiting the shop. Goodbye!")
            break

        else:
            print("Invalid option. Please choose again.")
            
def battle(player, monster):
    crit_meter = 0

    while player.health > 0 and monster.health > 0:
        crit_percentage = (crit_meter / 10) * 100
        print(f"Crit meter: {crit_percentage}%")
        print("1. Attack 2. Defend 3. Drink Potion 4. Run")
        answer = custom_input().lower()

        if answer == "attack" or answer == "1":
            if player.attack - monster.defense <= 0:
                monster.health -= 1
                print(f"You attacked the monster! Monster's health: {monster.health}")
            else:
                monster.health -= (player.attack - monster.defense)
                print(f"You attacked the monster! Monster's health: {monster.health}")
            crit_meter += 1

        elif answer == "defend" or answer == "2":
            if player.defense == 0:
                player.defense = 1
            player.defense *= 2
            print(f"You defended. Your defense is now {player.defense}.")
            crit_meter += 1

        elif answer == "drink potion" or answer == "3":
            available_potions = [potion for potion in player.inventory["potions"]]
            if available_potions:
                print("Available potions:")
                for i, potion in enumerate(available_potions):
                    print(f"{i}: {potion} - {player.format_item('potions', potion)}")
                potion_index = int(custom_input())
                potion = available_potions[potion_index]
                for stat, value in potion.items():
                    if stat == "health":
                        player.health += value
                        print(f"You drank a {potion}. Health increased by {value}.")
                    elif stat == "attack":
                        player.attack += value
                        print(f"You drank a {potion}. Attack increased by {value}.")
                    elif stat == "defense":
                        player.defense += value
                        print(f"You drank a {potion}. Defense increased by {value}.")
                player.inventory["potions"].remove(potion)
                crit_meter += 1
            else:
                print("You have no potions to drink.")

        elif answer == "run" or answer == "4":
            return "You ran away!", None

        elif answer == "exit":
            print("Exiting the game...")
            exit()

        if crit_meter >= 10:
            crit_meter = 0
            print("Critical Strike! You have an extra attack!")
            crit_damage = player.attack * 5
            monster.health -= crit_damage
            print(f"Critical hit! You dealt {crit_damage} damage to the monster. Monster's health: {monster.health}")

        if monster.health <= 0:
            loot = monster.drop_loot()
            return f"You have bested the {monster.name} in combat!", loot

        
        player.health -= max(0, monster.attack - player.defense)
        print(f"The monster attacked you for {monster.attack} damage. Your health: {player.health}")

        if player.health <= 0:
            return f"You have been defeated by the {monster.name}.", None
        else:
            player.defense = max(0, player.defense // 2)  #

    if player.defense > monster.attack:
        loot = monster.drop_loot()
        return f"The monster drops its weapon and runs away! It dropped: {player.format_item('weapons', loot['weapons'][0])}", loot

    loot = monster.drop_loot()
    return f"You have bested the {monster.name} in combat!", loot
