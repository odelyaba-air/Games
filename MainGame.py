from live import load_game, welcome


def main():
    user_name = "Guy"
    print(welcome(user_name))

    load_game()


if __name__ == "__main__":
    main()
