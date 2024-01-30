from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame

def welcome(user_name):
    return f"Welcome, {user_name}!"

def load_game():
    print("Welcome to the Game Center!")
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess the Number - guess the correct number within a given range.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    user_choice = input("Enter the number of your choice (1-3): ")
    difficulty_level = int(input("Enter the difficulty level (1 to 5): "))

    games = {
        "1": MemoryGame,
        "2": GuessTheNumber,  # Replace with your actual module/class for Guess the Number
        "3": CurrencyRouletteGame
    }

    selected_game = games.get(user_choice)

    if selected_game:
        game_instance = selected_game(difficulty_level)
        game_instance.play()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

# Script
from live import load_game, welcome

user_name = "Guy"
print(welcome(user_name))

load_game()
