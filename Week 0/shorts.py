# functions ==================================
def main():
    print("Hello, world!")
    print("This is CS50P.")


# main()


# return ======================================
def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"


# greeting = greet("how is the weather?")
# print("Hm, " + greeting)

# variables ====================================

def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")
    print(guess)


main()
