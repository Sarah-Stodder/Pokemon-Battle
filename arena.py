from trainer import Trainer
from pokemon import Pokemon
import ascii_magic
from colorizer import *
import time
from pyfiglet import figlet_format

class Arena():
    def __init__(self):
        self.trainer1= None
        self.trainer2= None

    def welcome(self):
        clear_screen()
        print('\n'*5)
        logo = ascii_magic.from_url('https://res.cloudinary.com/cae67/image/upload/v1657497449/pokemon_mdjxb5.png')
        ascii_magic.to_terminal(logo)
        print('\n'*2)
        input_yellow("\t\t\t\t\t\t --PRESS ENTER TO START--")
    
    
    def collect_team(self, trainer):
        while len(trainer.pokemon) < Trainer.MAX_TEAM_SIZE:
            print(Fore.BLUE if trainer.id%2== 0 else Fore.YELLOW, Style.BRIGHT, end =" ")
            clear_screen()
            poke_name = input(f"{trainer.name} What pokemon do you want to find?: ").title()
            if poke_name.lower() == "remove":
                poke_name = input(f'{trainer.name} What pokemon would you like to release?')
           
                if trainer.release(poke_name):
                    print(f'you have released {poke_name}')
                    time.sleep(2)
                else:
                    print(f" you haven't cought that pokemon!")
                    time.sleep(2)
                continue
           
            poke=Pokemon()
            if not poke.create_from_name(poke_name):
                print(f'{poke_name} is too elusive try another pokemon')
                time.sleep(2)
                continue
            clear_screen()
            print(f"{trainer.name} found {poke_name}")
            print(Style.RESET_ALL, end =" ")
            poke.display()
            print_red(poke.display_stats())
            if trainer.id%2==0:
                catchem = input_blue(f'Would you like to Catch {poke_name}? (Y/N) ')
            else:
                catchem = input_yellow(f'Would you like to Catch {poke_name}? (Y/N) ')

            if catchem and catchem[0].lower()== 'y':
                clear_screen()
                print_red(trainer.catch(poke))
                time.sleep(2)
                clear_screen()

    def battle_loop(self):
        while self.trainer1.pokemon and self.trainer2.pokemon:
            self.battle()
            clear_screen()

            player_1_dead = list(filter(lambda p: p.hit_points <= 0, self.trainer1.pokemon))
            player_2_dead = list(filter(lambda p: p.hit_points <= 0, self.trainer2.pokemon))

            if player_1_dead or player_2_dead:
                print_red(figlet_format("The Fallen", font="big"))

            if player_1_dead:
                print_yellow(figlet_format("PLAYER 1", font="starwars"))
                for poke in player_1_dead:
                    print_yellow(f"{poke.name} has been defeted")

            if player_2_dead:
                print_blue(figlet_format("PLAYER 2", font="starwars"))
                for poke in player_2_dead:
                    print_blue(f"{poke.name} has been defeted")
            

            self.trainer1.pokemon = list(filter(lambda p: p.hit_points > 0,self.trainer1.pokemon))
            self.trainer2.pokemon = list(filter(lambda p: p.hit_points > 0,self.trainer2.pokemon))
             
            if self.trainer1.pokemon or self.trainer2.pokemon:
                print_red(figlet_format("Remaining", font="big"))

            if self.trainer1.pokemon:
                print_yellow(figlet_format(f"{self.trainer1.name}", font="starwars"))
                for poke in self.trainer1.pokemon:
                    print_yellow(f'{poke.name} has {poke.hit_points} life remaining')


            if self.trainer2.pokemon:
                print_blue(figlet_format(f"{self.trainer2.name}", font="starwars"))
                for poke in self.trainer2.pokemon:
                    print_blue(f'{poke.name} has {poke.hit_points} life remaining')


            if self.trainer1.pokemon and self.trainer2.pokemon:
                input_red("\t\t\t\t --Press Enter For the Next Round--")
            else:
                input_green("\t\t\t\t --Press Enter--")

        if len(self.trainer1.pokemon)<=0:
            clear_screen()
            print_red(figlet_format(f"{self.trainer2.name} Claims Victory!",font="graffiti"))
          

        if len(self.trainer2.pokemon)<=0:
            clear_screen()
            print_red(figlet_format(f"{self.trainer1.name} Claims Victory!",font="graffiti"))
         


  
  
    def battle(self):
        trainer2_index = len(self.trainer2.pokemon) -1
        for index in range(len(self.trainer1.pokemon)):
            if trainer2_index >=0 and self.trainer1.pokemon[index].hit_points > 0 \
                and self.trainer2.pokemon[trainer2_index].hit_points >0:
                clear_screen()
                start_hp_p1 = self.trainer1.pokemon[index].hit_points
                start_hp_p2 = self.trainer2.pokemon[trainer2_index].hit_points
                
                self.trainer1.pokemon[index].attack(self.trainer2.pokemon[trainer2_index])

                self.trainer1.pokemon[index].display()
                print_yellow(figlet_format(f'\tHP {start_hp_p1}', font="doom"))
                time.sleep(2)
                clear_screen()
               
                self.trainer2.pokemon[trainer2_index].display()
                print_blue(figlet_format(f'\tHP {start_hp_p2}', font="doom"))
                time.sleep(2)
                clear_screen()

                logo = ascii_magic.from_url('https://res.cloudinary.com/cae67/image/upload/v1657666237/pokeball_closed_kqdsgd.png')
                ascii_magic.to_terminal(logo)
                time.sleep(1)
                clear_screen()
                logo = ascii_magic.from_url('https://res.cloudinary.com/cae67/image/upload/w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1657666100/pokeballopen_rtossk.png')
                ascii_magic.to_terminal(logo)
                time.sleep(1)
                clear_screen()

                damage_taken_p1 = int(self.trainer1.pokemon[index].hit_points - start_hp_p1)
                damage_taken_p2 = int(self.trainer2.pokemon[trainer2_index].hit_points - start_hp_p2)
                
                self.trainer1.pokemon[index].display(cols=40)
                print_yellow(figlet_format(f"{damage_taken_p1  if damage_taken_p1 else 'invincible'}", font="doom"))
               
                self.trainer2.pokemon[index].display(cols=40)
                print_blue(figlet_format(f"{damage_taken_p2 if damage_taken_p2 else 'invincible'}", font="doom"))
                time.sleep(2)
            trainer2_index-=1

#player one yellow
#player 2 blue
    def main(self):
        self.welcome()
        player_1 = input_yellow("Player 1 Enter Your Name: ").title()
        player_2 = input_blue("Player 2 Enter Your Name: ").title()
        self.trainer1=Trainer(player_1, 1)
        self.trainer2= Trainer(player_2, 2)

        print_yellow(f"""
        {self.trainer1.name} Capture Your Team
        You will get to capture up to {Trainer.MAX_TEAM_SIZE} Pokemon
        If you change your mind you can type remove to choose a Pokemon to release
        """
        )
        time.sleep(4)
        self.collect_team(self.trainer1)

        print_blue(f"""
        {self.trainer2.name} Capture Your Team
        You will get to capture up to {Trainer.MAX_TEAM_SIZE} Pokemon
        If you change your mind you can type remove to choose a Pokemon to release
        """
        )
        time.sleep(4)
        self.collect_team(self.trainer2)

        clear_screen()
        print_yellow(figlet_format(f"{self.trainer1.name}", font="starwars"))
        self.trainer1.show_team()
        time.sleep(3)


        clear_screen()
        print_blue(figlet_format(f"{self.trainer2.name}", font="starwars"))
        self.trainer2.show_team()
        time.sleep(3)

        self.battle_loop()




