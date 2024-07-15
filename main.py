class monster:
    def __init__(self, health, attack, defense, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.name = name
    
    def get_attack(self):
        return self.attack
    
    def  get_health(self):
        return self.health
    
    def get_defense(self):
        return self.defense
    
class player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.player_inventory = []
        self.gold_value = 0

    def get_health(self):
        return self.health
    
    def add_to_inventory(self, item):
        pass

    def sell_item(self, item):
        pass

loot = [
        {"rags": 10},
        {"staff of the mundane": 100}, 
        {"sword of the flu": 200}, 
        {"stick of truth": 400},
        {"greatsword of fire": 600},
        {"bow of aim-bot": 1000},
        {"ark of value": 7000}
        ] 

def main():
    pass
    
    
    
    
    
