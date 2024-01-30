import random
import time


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.sequence = []

    def generate_sequence(self):
        self.sequence = [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        user_list = []
        for _ in range(self.difficulty):
            user_input = input("Enter a number: ")
            while not user_input.isdigit():
                print("Invalid input. Please enter a valid number.")
                user_input = input("Enter a number: ")
            user_list.append(int(user_input))
        return user_list

    @staticmethod
    def is_list_equal(list1, list2):
        return list1 == list2

    def play(self):
        print("Memorize the sequence...")
        time.sleep(0.7)
        self.generate_sequence()

        print("Now, enter the numbers:")
        user_input_list = self.get_list_from_user()

        if MemoryGame.is_list_equal(user_input_list, self.sequence):
            print("Congratulations! You won!")
            return True
        else:
            print("Sorry, you lost. Better luck next time.")
            return False


difficulty_level = int(input("Enter the difficulty level (1 to 5): "))
game = MemoryGame(difficulty_level)
game_result = game.play()
