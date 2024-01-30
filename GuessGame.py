import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                user_guess = int(input(f"Enter your guess (between 1 and {self.difficulty}): "))
                if 1 <= user_guess <= self.difficulty:
                    return user_guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def compare_results(self, user_guess):
        return user_guess == self.secret_number

    def play(self):
        self.generate_number()
        print(f"Guess the secret number between 1 and {self.difficulty}")

        while True:
            guess = self.get_guess_from_user()

            if self.compare_results(guess):
                print("Congratulations! You guessed the correct number.")
                return True
            else:
                print("Wrong guess. Try again.")


# Example usage:
if __name__ == "__main__":
    difficulty_level = 3
    game = GuessGame(difficulty_level)
    result = game.play()

    if result:
        print("You won!")
    else:
        print("You lost!")
