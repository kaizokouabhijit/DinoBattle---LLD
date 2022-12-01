import numpy as np
import json

f = open('Dino_stats.json')
dino_data = json.load(f)


# for obj in dino_data:
#     print(dino_data[obj]["Health"])



class Dino:

    def __init__(self) -> None:
        
        pass
    def __init__(self,  dino_name, choice) -> None:
        self.name = dino_name
        if choice == 1:
            key ="T-Rex"
        elif choice == 2:
            key ="Stegosaurus"
        else:
            key = "Triceratops"

        self.Health = dino_data[key]["Health"]
        self.damage_min_a = dino_data[key]["damage_min_a"]
        self.damage_min_d = dino_data[key]["damage_min_d"]
        self.damage_max_a = dino_data[key]["damage_max_a"]
        self.damage_max_d = dino_data[key]["damage_max_d"]
        self.defense_min_a = dino_data[key]["defense_min_a"]
        self.defense_min_d = dino_data[key]["defense_min_d"]
        self.defense_max_a = dino_data[key]["defense_max_a"]
        self.defense_max_d = dino_data[key]["defense_max_d"]
        self.key = key

    
    def get_attack(self, choice):
        # self.mode = 'Damage'
        if choice ==1:
            attack = int(np.random.randint(self.damage_min_a, self.damage_max_a+1, 1))
            return attack
        else:
            return int(np.random.randint(self.damage_min_d, self.damage_max_d+1, 1))

    def get_defense(self, choice):
        if choice ==1:
            return int(np.random.randint(self.defense_min_a, self.defense_max_a+1, 1))
        else:
            return int(np.random.randint(self.defense_min_d, self.defense_max_d+1, 1))

    def adjust_health(self, attack, defense):
        self.Health = self.Health - attack+defense
        return self.Health

            

    def print_health(self):
        print(f'Health remaining for {self.name} is {self.Health}')

    def print_stats(self):
        print(f"{self.name}")
        print(f"\tHealth: {self.Health}")
        print(f"\tMin Damage while attacking: {self.damage_min_a}")
        print(f"\tMin Damage while defending: {self.damage_min_d}")
        print(f"\tMax Damage while attacking:{self.damage_max_a}")
        print(f"\tMax Damage while defending:{self.damage_max_d}")
        print(f"\tMin defense while attacking:{self.defense_min_a}")
        print(f"\tMin defense while defending:{self.defense_min_d}")
        print(f"\tMax defense while attacking:{self.defense_max_a}")
        print(f"\tMax Damage while defending:{self.defense_max_d}")