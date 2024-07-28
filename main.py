from player import *
from monster import *
from tkinter import *
from loot import *
from shop_and_battle import *
from story_prompt import *

def main():
    story_prompt()
    hero = Player(10, 3, 0)
    print("Please enter your name")
    hero.name = input()
    print(f"Welcome {hero.name.title()}, you have {hero.health} health, you deal {hero.attack} damage, and you can defend against {hero.defense} damage. Where would you like to go on your journey?")
    while hero.get_total_gold() < 1000:
        monster = Monster()
        monster.create_monster()
        fight_result, loot = battle(hero, monster)
        print(fight_result)
        print(f"your health: {hero.health}")
        if hero.get_total_gold() == 500:
            print("half way there hero!")
            continue
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
                answer = input().lower()
                if answer == "y":
                    hero.pick_up_loot(loot)
                    break
                elif answer == "n":
                    break
                elif answer == "show gold":
                    hero.display_gold()
                else:
                    print("Invalid option. Please enter 'y', 'n', or 'show gold'.")
        
        if hero.health < 100:
            while True:
                print("Would you like to go to town and rest? y/n")
                rest_answer = input().lower()
                if rest_answer == "y":
                    hero.rest()
                    print("Would you like to visit the shop while you're here? y/n")
                    shop_answer = input().lower()
                    if shop_answer == "y":
                        shop(hero)
                    break
                elif rest_answer == "n":
                    break
                elif rest_answer == "show gold":
                    hero.display_gold()
                else:
                    print("Invalid option. Please enter 'y', 'n', or 'show gold'.")
        
        while True:
            print("Would you like to equip items, see how much gold you have, check your stats, or exit inventory? (equip/show gold/check/exit)")
            action = input().lower()
            if action == "equip":
                print("Would you like to equip a weapon, armor, or shield? (weapons/armor/shields)")
                item_type = input().lower()
                if item_type == "weapons" and hero.inventory['weapons']:
                    print("Which weapon would you like to equip?")
                    for i, weapon in enumerate(hero.inventory['weapons']):
                        print(f"{i}: {hero.format_item('weapons', weapon)}")
                    weapon_index = int(input())
                    hero.equip_weapon(weapon_index)
                elif item_type == "armor" and hero.inventory['armor']:
                    print("Which armor would you like to equip?")
                    for i, armor in enumerate(hero.inventory['armor']):
                        print(f"{i}: {hero.format_item('armor', armor)}")
                    armor_index = int(input())
                    hero.equip_armor(armor_index)
                elif item_type == "shields" and hero.inventory['shields']:
                    print("Which shield would you like to equip?")
                    for i, shield in enumerate(hero.inventory['shields']):
                        print(f"{i}: {hero.format_item('shields', shield)}")
                    shield_index = int(input())
                    hero.equip_shield(shield_index)
                else:
                    print("Invalid option or no items available to equip.")
            elif action == "show gold":
                hero.display_gold()
            elif action == "check":
                print(f"your attack is: {hero.get_attack_stat()}, and your defense is: {hero.get_defense_stat()}")
            elif action == "exit":
                break
            else:
                print("Invalid option. Please choose again.")
        
        print("Would you like to continue on your journey? y/n")
        continue_answer = input().lower()
        if continue_answer == "n":
            break
    
    if hero.get_total_gold() >= 1000:
        print("Congratulations! You have accumulated 1000 gold your town will be safe and well fed!")
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
