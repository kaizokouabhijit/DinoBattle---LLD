import numpy as np
import json
from Dino import Dino

f = open('Dino_stats.json')
dino_data = json.load(f)



class DinoBattle:
    def __init__(self):
        print("Details of the Dinos are: ")
        for obj in dino_data:
            print(f"for dino {obj}:")

            print(f"\t Health: {dino_data[obj]['Health']}")

            print(f"\t Min and max damage while aggressive : {dino_data[obj]['damage_min_a']} - {dino_data[obj]['damage_max_a']}")
            
            print(f"\t Min and Max damage while defensive: {dino_data[obj]['damage_min_d']} - {dino_data[obj]['damage_max_d']}")        
            
            print(f"\t Min and Max defense while aggressive: {dino_data[obj]['defense_min_a']} - {dino_data[obj]['defense_max_a']}")
    
            print(f"\t Min and Max defense while defensive: {dino_data[obj]['defense_min_d']} - {dino_data[obj]['defense_max_d']}")


        player_choice = int(input("To select a dinosaur: Enter 1 for T-Rex, 2 for Stegosaurus, 3 for Triceratops: "))
        
        if player_choice not in [1,2,3]:
            raise Exception("Enter only from 1,2,3")
        
        comp_choice = np.random.randint(1,4,1)
        while(comp_choice == player_choice):
            comp_choice = np.random.randint(1,4,1)
            
        dino_name = str(input("Enter the dino name: "))
        player_dino = Dino(dino_name, player_choice)
        print(f"You chose {player_dino.key} - {player_dino.name}")
                
        comp_dino = Dino("Comp_dino", comp_choice)
        print(f"Computer chose {comp_dino.key} - {comp_dino.name}")
        self.game(player_dino, comp_dino)



    def game(self,player_dino, comp_dino):
        print("Let's Begin!!")

        player_dino.print_stats()
        comp_dino.print_stats()

        comp_guess = np.random.randint(1,11,1)
        player_guess = int(input("Computer has guessed a number, press 1 if you think it's Even, else press 2 for odd. If you are right, you get to go first!!"))
        if(comp_guess%2==0 and player_guess ==1) or (comp_guess%2==1 and player_guess ==2):
            print("Player goes first")
            self.moves(player_dino, comp_dino)

        else:
            print("comp goes first")
            self.moves(player_dino, comp_dino)


    def moves(self, player_dino, comp_dino):
        while(player_dino.Health >0 and comp_dino.Health >0):
            player_move_choice = int(input("Enter 1 for agressive move and 2 for defensive move"))
            comp_move_choice = np.random.randint(1,3,1)
            print(f"comp choice - {comp_move_choice}")

            player_attack = player_dino.get_attack(player_move_choice)
            player_defence = player_dino.get_defense(player_move_choice)

            comp_attack = comp_dino.get_attack(comp_move_choice)
            comp_defence = comp_dino.get_defense(comp_move_choice)

            player_dino.adjust_health(comp_attack,player_defence)
            comp_dino.adjust_health(player_attack,comp_defence)

            print(f"{player_dino.name} attack value is {player_attack}")
            print(f"{player_dino.name} defense value is {player_defence}")
            player_dino.print_health()
            print(f"Comp_dino attack value is {comp_attack}")
            print(f"Comp_dino defense value is {comp_defence}")            
            comp_dino.print_health()
        if player_dino.Health <= 0 and comp_dino.Health <=0:
            print("Draw")
            repeat_choice = int(input("Wanna play again? Enter 1 for Yes and 2 for No "))
            if repeat_choice == 1:
                self.__init__()
            else:
                print("Thanks for playing!")

        elif player_dino.Health <=0:
            print("Comp wins")
            repeat_choice = int(input("Wanna play again? Enter 1 for Yes and 2 for No "))
            if repeat_choice == 1:
                self.__init__()
            else:
                print("Thanks for playing!")
        else:
          print("player wins")
          repeat_choice = int(input("Wanna play again? Enter 1 for Yes and 2 for No "))
          if repeat_choice == 1:
                self.__init__()
          else:
                print("Thanks for playing!")


    
    




if __name__ == '__main__':
    DinoBattle()