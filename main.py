from player import *
from monster import *
from tkinter import *
from loot import *
from shop_and_battle import *

def main():
    print("Please enter your name")
    hero = Player(100, 10, 5)
    hero.name = input().strip()
    print(f"Welcome {hero.name.title()}, you have {hero.health} health, you deal {hero.attack} damage, and you can defend against {hero.defense} damage. Where would you like to go on your journey?")
    
    while hero.get_total_gold() < 1000:
        monster = Monster()
        monster.create_monster()
        fight_result, loot = battle(hero, monster)
        print(fight_result)
        
        if hero.health <= 0:
            print("You have been defeated. Game Over!")
            break
        
        if loot:
            print("They have dropped:")
            for loot_type, items in loot.items():
                for item in items:
                    print(hero.format_item(loot_type, item))
            
            print("Would you like to pick those items up? y/n")
            answer = input().lower()
            if answer == "y":
                hero.pick_up_loot(loot)
        
        if hero.health < 100:
            print("Would you like to go to town and rest? y/n")
            rest_answer = input().lower()
            if rest_answer == "y":
                hero.rest()
                print("Would you like to visit the shop while you're here? y/n")
                shop_answer = input().lower()
                if shop_answer == "y":
                    shop(hero)
        
        while True:
            print("Would you like to equip items, sell items, or continue your journey? (equip/sell/continue)")
            equip_or_sell_answer = input().lower()
            if equip_or_sell_answer == "equip":
                print("Would you like to equip a weapon, armor, or shield? (weapons/armor/shields)")
                item_type = input().lower()
                if item_type == "weapons":
                    if hero.inventory['weapons']:
                        print("Which weapon would you like to equip?")
                        for i, weapon in enumerate(hero.inventory['weapons']):
                            print(f"{i}: {hero.format_item('weapons', weapon)}")
                        try:
                            weapon_index = int(input())
                            if 0 <= weapon_index < len(hero.inventory['weapons']):
                                hero.equip_weapon(weapon_index)
                            else:
                                print("Invalid index.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    else:
                        print("No weapons available to equip.")
                elif item_type == "armor":
                    if hero.inventory['armor']:
                        print("Which armor would you like to equip?")
                        for i, armor in enumerate(hero.inventory['armor']):
                            print(f"{i}: {hero.format_item('armor', armor)}")
                        try:
                            armor_index = int(input())
                            if 0 <= armor_index < len(hero.inventory['armor']):
                                hero.equip_armor(armor_index)
                            else:
                                print("Invalid index.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    else:
                        print("No armor available to equip.")
                elif item_type == "shields":
                    if hero.inventory['shields']:
                        print("Which shield would you like to equip?")
                        for i, shield in enumerate(hero.inventory['shields']):
                            print(f"{i}: {hero.format_item('shields', shield)}")
                        try:
                            shield_index = int(input())
                            if 0 <= shield_index < len(hero.inventory['shields']):
                                hero.equip_shield(shield_index)
                            else:
                                print("Invalid index.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    else:
                        print("No shields available to equip.")
                else:
                    print("Invalid option or no items available to equip.")
            elif equip_or_sell_answer == "sell":
                sellable_items = hero.get_sellable_items()
                if not sellable_items:
                    print("No items available to sell.")
                    break
                print("Which item would you like to sell?")
                for i, (loot_type, item) in enumerate(sellable_items):
                    item_name, item_stats = item
                    gold_value = item_stats.get("gold-value", 0)
                    print(f"{i}: {hero.format_item(loot_type, item)} (worth {gold_value} gold)")
                try:
                    item_index = int(input())
                    if 0 <= item_index < len(sellable_items):
                        loot_type, item = sellable_items[item_index]
                        hero.sell_item(loot_type, item_index)
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif equip_or_sell_answer == "continue":
                break
            else:
                print("Invalid option. Please choose again.")
        
        print("Would you like to continue on your journey? y/n")
        continue_answer = input().lower()
        if continue_answer == "n":
            break
    
    if hero.get_total_gold() >= 1000:
        print("Congratulations! You have accumulated 1000 gold and won the game!")
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
