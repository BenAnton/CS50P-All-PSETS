
def main():
    text = input("Please enter a string: ")
    short_text = shorten(text)
    print(short_text)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    short_text = ""

    for char in word:
        if char not in vowels:
            short_text += char

    return(short_text)


if __name__ == "__main__":
    main()
