text = input("Please enter a string: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
short_text = ""

for char in text:
    if char not in vowels:
        short_text += char

print(short_text)

