import random
import sys


def main():
    level = get_level()
    score = play(level)
    print(f"Score: {score}")


# Get level from user
def get_level():
    while True:
        try:
            level = int(input())
            if level == 1 or level == 2 or level == 3:
                print(f"Level: {level}")
                return level
        except ValueError:
            print("Invalid Input")


# Generate the numbers based on difficulty
def generate_integer(level):
    difficulty = ""
    if level == 1:
        difficulty = 9
        X = random.randint(0, difficulty)
        Y = random.randint(0, difficulty)
        return X, Y
    elif level == 2:
        difficulty = 99
        X = random.randint(10, difficulty)
        Y = random.randint(10, difficulty)
        return X, Y
    else:
        difficulty = 999
        X = random.randint(100, difficulty)
        Y = random.randint(100, difficulty)
        return X, Y


# Generate the sum and answer
def generate_sum(level):
    X, Y = generate_integer(level)
    sum = str(f"{X} + {Y} = ")
    answer = X + Y
    return sum, answer


# play the game
def play(level):
    sum_counter = 0
    score = 0

    # loop ten times to increment of sum_counter
    while sum_counter < 10:
        # get inputs
        sum, answer = generate_sum(level)
        #  initialise attemps to zero
        attempts = 0
        # attempts three times
        while attempts < 3:
            try:
                # to get user input
                user_input = int(input(sum))
                # if correct increase score and sum_counter then break the loop
                if user_input == answer:
                    score += 1
                    break
                # if not correct print EEE, and increase attempts
                else:
                    print("EEE")
                    attempts += 1
            # if value error then also increase attempts
            except ValueError:
                print("EEE")
                attempts += 1
            # when attempts reach 3 print the answer and increase sum count, reset the attempts
        if attempts == 3:
            print(answer)
            attempts = 0
        # increment the sum counter
        sum_counter += 1

    # return the score to main for printing.
    return score


if __name__ == "__main__":
    main()
