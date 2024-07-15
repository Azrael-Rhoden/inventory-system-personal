import random
from player import *
from monster import *
    
def main():
    hero = Player(10,5,2)
    monster = Monster(10, 2, 3, "goblin")
    monster.deal_damage_player(hero)


def battle(monster):
    print(f"on your travels you come across a {monster}!\nwhat do you do?")
    print("1.fight\n2.run\n")
    choice = input()

    if choice == 2:
        return "you ran"
    if choice == 1:
        pass
    else:
        raise Exception("invalid input please try again")
    
main()