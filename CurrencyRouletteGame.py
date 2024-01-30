import random
import requests


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.api_key = "YOUR_API_KEY"  # Replace with your actual API key

    def get_money_interval(self):
        try:
            url = f"https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey={self.api_key}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            exchange_rate = response.json()["USD_ILS"]

            total_value_of_money = random.randint(1, 100)
            lower_bound = total_value_of_money - (5 - self.difficulty)
            upper_bound = total_value_of_money + (5 - self.difficulty)

            return exchange_rate * lower_bound, exchange_rate * upper_bound
        except requests.exceptions.RequestException as e:
            print(f"Error getting exchange rate: {e}")
            raise  # Re-raise the exception for the caller

    @staticmethod
    def get_guess_from_user():
        user_guess = input("Enter your guess for the value in ILS: ")
        while not user_guess.replace('.', '').isdigit():
            print("Invalid input. Please enter a valid numeric value.")
            user_guess = input("Enter your guess for the value in ILS: ")
        return float(user_guess)

    def play(self):
        print("Welcome to Currency Roulette!")
        print("Try to guess the value of a random amount in USD to ILS.")

        try:
            lower_limit, upper_limit = self.get_money_interval()
            random_value = random.uniform(lower_limit, upper_limit)

            user_guess = self.get_guess_from_user()

            print(f"The correct value is: {random_value} ILS")

            if lower_limit <= user_guess <= upper_limit:
                print("Congratulations! You won!")
                return True
            else:
                print("Sorry, you lost. Better luck next time.")
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


# Example usage
difficulty_level = int(input("Enter the difficulty level (1 to 5): "))
game = CurrencyRouletteGame(difficulty_level)
game_result = game.play()
