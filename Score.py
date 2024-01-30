import os

POINTS_OF_WINNING = 0


def add_score(difficulty):
    try:
        if os.path.exists('Scores.txt'):
            with open('Scores.txt', 'r') as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0
            with open('Scores.txt', 'w') as file:
                file.write(str(current_score))

        points_for_winning = (difficulty * 3) + 5
        new_score = current_score + points_for_winning

        with open('Scores.txt', 'a') as file:
            file.write(str(new_score) + '\n')

        return new_score

    except Exception as e:
        print(f"Error adding score: {e}")
        return None
