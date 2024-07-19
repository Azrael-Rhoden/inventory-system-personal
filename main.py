from player import *
from monster import *
    
def battle(hero, monster):
    print(f"On your travels you come across a {monster.name}!\nWhat do you do?")
    print(f"This monster has {monster.health} health, {monster.attack} damage, and {monster.defense} protection")
    while True:
        print("1. Fight\n2. Run\n")
        choice = input()

        if choice == "run":
            return "You ran"
        elif choice == "fight":
            if hero.defense >= monster.attack:
                return "Your armor was greater than their offense! They cannot hurt you.\nThey have dropped their weapon."
            while hero.health > 0 and monster.health > 0:
                hero.deal_damage_monster(monster)
                print(f"{monster.name}'s health: {monster.health}")
                if monster.health > 0:
                    monster.deal_damage_player(hero)
                    print(f"{hero.name}'s health: {hero.health}")
                if monster.health <= 0:
                    return "You have bested them in combat!"
                if hero.health <= 0:
                    return "You have died!"
        else:
            print("Invalid input. Please try again.")
        continue

def main():
    print("Please enter your name")
    hero = Player(10, 5, 3)
    print(f"Welcome {hero.name}, your have {hero.health} health, you deal {hero.attack} damage, and you can defend against {hero.defense} damage. Where would you like to go on your journey?")
    monster = Monster()
    monster.create_monster()
    print(f"Monster after creation: {monster.name}, Health: {monster.health}, Attack: {monster.attack}, Defense: {monster.defense}")
    fight = battle(hero, monster)
    print(fight)

if __name__ == "__main__":
    main()