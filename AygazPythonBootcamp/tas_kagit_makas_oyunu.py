import random

class Rock_Paper_Scissors_Game:

    def __init__(self):
        self.answer_list = ("rock", "paper", "scissors")
        self.player1_defeat_counter = 0
        self.player2_defeat_counter = 0
        self.player1_choice = ""
        self.player2_choice = ""
        self.game_over_message = ""
        self.is_game_over = False
        self.keep_playing_options = ("yes","no")
        self.player1_continue = ""
        self.player2_continue = ""


    def greetings_and_rules(self):
     print("Welcome to Rock, Paper and Scissors Game. \nIn this game each user choose one of the three options which are Rock, Paper and Scissors. \nRock defeats Scissors, Scissors defeats Paper and Paper defeats Rock \nIf a user wins two consecutive rounds the game is over. \nIf you type 'quit' you can close the game whenever you want")


    def get_player_choice(self):
        self.player1_choice = input("Type your choice (rock, paper, scissors): ").lower()
        self.player2_choice = random.choice(self.answer_list)
        print("Player 2 choice:", self.player2_choice)

        if self.player1_choice not in self.answer_list and self.player1_choice != "quit":
            print("*****************************\nINVALID INPUT - Please enter 'rock', 'paper', or 'scissors'.\n*****************************")
            return False
        return True

    def determine_winner(self):
        if self.player1_choice == "rock" and self.player2_choice == "paper":
            print("Player 2 won")
            self.player2_defeat_counter += 1
        elif self.player1_choice == "rock" and self.player2_choice == "scissors":
            print("Player 1 won")
            self.player1_defeat_counter += 1
        elif self.player1_choice == "paper" and self.player2_choice == "rock":
            print("Player 1 won")
            self.player1_defeat_counter += 1
        elif self.player1_choice == "paper" and self.player2_choice == "scissors":
            print("Player 2 won")
            self.player2_defeat_counter += 1
        elif self.player1_choice == "scissors" and self.player2_choice == "rock":
            print("Player 2 won")
            self.player2_defeat_counter += 1
        elif self.player1_choice == "scissors" and self.player2_choice == "paper":
            print("Player 1 won")
            self.player1_defeat_counter += 1
        elif self.player1_choice == self.player2_choice:
            print("It's a tie!")
        else:
            print("*****************************\n PLAYER QUITS THE GAME \n*****************************")
            self.is_game_over = True

    def check_game_over(self):
        if self.player1_defeat_counter >= 2:
            self.is_game_over = True
            print("Player 1 is the overall winner!")
        elif self.player2_defeat_counter >= 2:
            self.is_game_over = True
            print("Player 2 is the overall winner!")

    def quit_game_anytime(self):
        if self.get_player_choice == "quit":
         self.is_game_over = True

    def keep_playing_or_not(self):
        self.player1_continue = input("GAME OVER! Do you want to continue playing? Type Yes/No: ").lower()
        self.player2_continue = random.choice(self.keep_playing_options)
        print("Player 2 continue:", self.player2_continue)

        if self.player1_continue == "no":
          self.game_over_message = "no"
          return False
        elif self.player2_continue == "no":
          self.game_over_message = "no"
          return False
        elif self.player1_continue not in self.keep_playing_options:
          input("*****************************\nINVALID INPUT - Please enter 'Yes' or 'No'.\n*****************************")
          return False
        elif self.player2_continue not in self.keep_playing_options:
          input("*****************************\nINVALID INPUT - Please enter 'Yes' or 'No'.\n*****************************")
          return False
        else:
         return True

    def reset_game(self):
        self.player1_defeat_counter = 0
        self.player2_defeat_counter = 0
        self.is_game_over = False
        print("Game reset. Let's play again!")

    def rock_paper_scissors_EfeCagri_Sen(self):
        self.greetings_and_rules()
        while not self.is_game_over:
            if self.get_player_choice():
              self.quit_game_anytime()
              self.determine_winner()
              self.check_game_over()
              if self.is_game_over:
                if self.keep_playing_or_not():
                  self.reset_game()
                else:
                    break

game = Rock_Paper_Scissors_Game()
game.rock_paper_scissors_EfeCagri_Sen()
