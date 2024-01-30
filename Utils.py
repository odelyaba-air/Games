import os


SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# Example usage:
if __name__ == "__main__":
    screen_cleaner()
    print("Screen cleared!")
