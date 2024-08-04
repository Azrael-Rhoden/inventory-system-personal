from player import *
from main import *

def custom_input(prompt=""):
    user_input = input(prompt)
    if user_input.lower() == "exit":
        print("Exiting the game. Goodbye!")
        exit()
    return user_input

def shop(hero):
    shop_inventory = {
        "weapons": {
            "Sword": {"attack": 5, "value": 100},
            "Axe": {"attack": 7, "value": 150}
        },
        "armor": {
            "Chainmail": {"defense": 5, "value": 100},
            "Plate": {"defense": 7, "value": 150}
        },
        "shields": {
            "Wooden Shield": {"defense": 3, "value": 50},
            "Iron Shield": {"defense": 5, "value": 100}
        },
        "potions": {
            "Health Potion": {"healing": 20, "value": 50}
        }
    }

    while True:
        print("Would you like to buy or sell items? (buy/sell/exit)")
        action = custom_input().lower()
        if action == "buy":
            while True:
                print("Items available for purchase:")
                for category, items in shop_inventory.items():
                    for i, (item_name, item_stats) in enumerate(items.items()):
                        print(f"{i}: {item_name} - {item_stats['value']} gold")
                print("Which item would you like to buy? (enter the item number or type 'exit' to leave)")
                item_index = custom_input()
                if item_index.lower() == "exit":
                    break
                if item_index.lower() == "show gold":
                    hero.display_gold()
                    continue
                item_index = int(item_index)
                category = list(shop_inventory.keys())[item_index // len(list(shop_inventory.values())[0])]
                item_name, item_stats = list(shop_inventory[category].items())[item_index % len(list(shop_inventory.values())[0])]
                if hero.gold >= item_stats["value"]:
                    hero.gold -= item_stats["value"]
                    hero.add_item_to_inventory(item_name, item_stats)
                    print(f"You have purchased {item_name}!")
                else:
                    print("You do not have enough gold to buy this item.")
        elif action == "sell":
            sellable_items = hero.get_sellable_items()
            if not sellable_items:
                print("You have no items to sell.")
                continue
            while True:
                print("Items in your inventory:")
                for i, (loot_type, item) in enumerate(sellable_items):
                    item_name, item_stats = item
                    gold_value = item_stats.get("value", 0)
                    print(f"{i}: {hero.format_item(loot_type, item)} (worth {gold_value} gold)")
                print("Which item would you like to sell? (enter the item number or type 'exit' to leave)")
                item_index = custom_input()
                if item_index.lower() == "exit":
                    break
                if item_index.lower() == "show gold":
                    hero.display_gold()
                    continue
                item_index = int(item_index)
                loot_type, item = sellable_items[item_index]
                hero.sell_item(loot_type, item_index)
        elif action == "exit":
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
