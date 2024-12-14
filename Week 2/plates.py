numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (
    min_max(s) and
    starts_with_letters(s) and
    ends_with_numbers(s) and
    punctuation_check(s)
    )

def min_max(s):
    return 2 <= len(s) <= 6

def starts_with_letters(s):
    return s[0] in letters and s[1] in letters

def ends_with_numbers(s):
    is_number_found = False

    for char in s:
        if char in numbers:
            if not is_number_found:
                if char == "0":
                    return False
            is_number_found = True
        elif is_number_found:
            return False

    return True

def punctuation_check(s):
    for char in s:
        if char not in numbers and char not in letters:
            return False
    return True

main()
