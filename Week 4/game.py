import random
import sys


def main():
    level = setup_game()
    while True:
        guess = get_guess()
        play_game(level, guess)


def setup_game():
    while True:
        try:
            level = int(input("Please give a positive integer to set the level: "))
            if level > 0:
                level = random.randrange(1, level)
                print(f"Level is now set at {level}")
                return level
        except ValueError:
            print("Positive Integer Required")


def get_guess():
    while True:
        try:
            guess = int(input("Please enter your next guess: "))
            if guess > 0:
                return guess
        except ValueError:
            print("Please enter a positive number")


def play_game(level, guess):
    if guess > level:
        print("Too large!")

    elif guess < level:
        print("Too small!")

    else:
        print("Just right!")
        sys.exit()


main()
