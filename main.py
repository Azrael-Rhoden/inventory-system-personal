from player import *
from monster import *
from tkinter import *
from loot import *
from shop_and_battle import *
from story_prompt import *

def main():
    story_prompt()
    print("Please enter your name")
    hero = Player(10, 2, 0)  
    hero.name = input()
    hero.update_attack_defense()
    print(f"Welcome {hero.name.title()}, you have {hero.health} health, you deal {hero.attack} damage with a {hero.equipped_weapon[0][0:]}, and you can defend against {hero.defense} damage. Where would you like to go on your journey?")

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

            while True:
                print("Would you like to pick those items up? y/n")
                answer = custom_input().lower()
                if answer == "show gold":
                    hero.display_gold()
                    continue
                if answer == "y":
                    hero.pick_up_loot(loot)
                    break
                if answer == "n":
                    break

        if hero.health < 100:
            while True:
                print("Would you like to go to town and rest? y/n")
                rest_answer = custom_input().lower()
                if rest_answer == "show gold":
                    hero.display_gold()
                    continue
                if rest_answer == "y":
                    hero.rest()
                    while True:
                        print("Would you like to visit the shop while you're here? y/n")
                        shop_answer = custom_input().lower()
                        if shop_answer == "show gold":
                            hero.display_gold()
                            continue
                        if shop_answer == "y":
                            shop(hero)
                            break
                        if shop_answer == "n":
                            break
                    break
                if rest_answer == "n":
                    break

            

        while True:
            print("Would you like to equip items, sell items, or continue your journey? (equip/sell/continue)")
            equip_or_sell_answer = custom_input().lower()
            if equip_or_sell_answer == "show gold":
                hero.display_gold()
                continue
            if equip_or_sell_answer == "equip":
                print("Would you like to equip a weapon, armor, or shield? (weapons/armor/shields)")
                item_type = custom_input().lower()
                if item_type == "show gold":
                    hero.display_gold()
                    continue
                if item_type == "weapons" and hero.inventory["weapons"]:
                    print("Which weapon would you like to equip?")
                    for i, weapon in enumerate(hero.inventory["weapons"]):
                        print(f"{i}: {hero.format_item('weapons', weapon)}")
                    weapon_index = int(custom_input())
                    hero.equip_weapon(weapon_index)
                elif item_type == "armor" and hero.inventory["armor"]:
                    print("Which armor would you like to equip?")
                    for i, armor in enumerate(hero.inventory["armor"]):
                        print(f"{i}: {hero.format_item('armor', armor)}")
                    armor_index = int(custom_input())
                    hero.equip_armor(armor_index)
                elif item_type == "shields" and hero.inventory["shields"]:
                    print("Which shield would you like to equip?")
                    for i, shield in enumerate(hero.inventory["shields"]):
                        print(f"{i}: {hero.format_item('shields', shield)}")
                    shield_index = int(custom_input())
                    hero.equip_shield(shield_index)
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
                    gold_value = item_stats.get("value", 0)
                    print(f"{i}: {hero.format_item(loot_type, item)} (worth {gold_value} gold)")
                item_index = custom_input()
                if item_index.lower() == "show gold":
                    hero.display_gold()
                    continue
                if item_index.lower() == "exit":
                    break
                item_index = int(item_index)
                loot_type, item = sellable_items[item_index]
                hero.sell_item(loot_type, item_index)
            elif equip_or_sell_answer == "continue":
                break
            else:
                print("Invalid option. Please choose again.")
        
    if hero.get_total_gold() >= 1000:
        print("Congratulations! You have accumulated 1000 gold and won the game!")
    else:
        print("Thanks for playing!")



if __name__ == "__main__":
    main()
