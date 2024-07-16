class Player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.player_inventory = []
        self.gold_value = 0
        self.name = input()

    def deal_damage_monster(self,other):
        other.health -= self.attack -  other.defense

    