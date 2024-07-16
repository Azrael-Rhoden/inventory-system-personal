from player import *
from monster import *
    
def main():
    print("please enter your name")
    hero = Player(20,10,5)
    print(f"Welcome {hero.name} your health is {hero.health} your attack power is {hero.attack} and your defense is {hero.defense} where would you like to go on your journey?")
    monster = Monster(20, 0, 0, "goblin")
    fight = battle(hero, monster)
    print(fight)


def battle(hero,monster):
    print(f"on your travels you come across a {monster.name}!\nwhat do you do?")
    while True:
        print("1.fight\n2.run\n")
        choice = input()

        if choice == "run":
            return "you ran"
        if choice == "fight":
            if hero.defense >= monster.attack:
                return "Your armor was greater than their offense! They cannot hurt you.\nthey have dropped their weapon"
            if hero.health > 0 and monster.health > 0:
                hero.deal_damage_monster(monster)
                print(f"{monster.name}`s health: {monster.health}")
                if monster.health > 0:
                    monster.deal_damage_player(hero)
                    print(f"{hero.name}`s health: {hero.health}")
                if monster.health <= 0:
                    return "You have bested them in combat!"
                if hero.health <= 0:
                    return "You have died!"
        else:
            print("invalid input please try again")
        continue
    
main()