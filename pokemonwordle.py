from argparse import ArgumentParser
import pandas as pd
import random
import re
import sys



def play_game():
  correct_answer = random.choice()
  lives = 5
  while lives > 0:
    guess = input("Guess a Pokemon: ")
    if guess = correct answer:
      print(f"Correct! The Pokemon is {correct_answer}")
    else:
      lives -=1
      print(f"Incorrect, you have {lives} guesses left")
    if lives == 0:
      print(f"You ran out of guesses, the Pokemon was {correct_answer}")
  play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
      play_game()
    else:
      print("Thanks for playing!")
      
                     
    #file opening and iteration                 
                     
    def pokemon_wordle(file):
  with open('pokemon.csv', encoding = 'utf -8') as f:
    df = pd.read_csv(f)
    new_df = df.drop(['HP','Total', 'Attack', 'Defense', 'Sp. Def', 'Speed', 'Sp. Atk' ], 
                 axis = 1)
    for name in new_df['Name']:
      game_choice = rand.choice(new_df['Name'])
  return game_choice


  test = pokemon_wordle

    



              
  
  

 
if __name__ == '__main__':
  main()
  
