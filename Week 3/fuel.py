def main():
    result = check_input_int()

    if result is None:
        print("Input Invalid")
    else:
        X, Y = result
        percentage = get_percentage(X, Y)

        if percentage == "E":
            print("E")
        elif percentage == "F":
            print("F")
        else:
            print(f"{percentage}%")


def check_input_int():
    while True:
        try:
            fraction = input("Please enter a fraction formatted X/Y: ")
            X, Y = map(int, fraction.split("/"))

            if Y == 0:
                continue

            if  X > Y:
                continue

            return X, Y

        except ValueError:
            continue

def get_percentage(X, Y):
    percentage = (X / Y) * 100
    rounded_percentage = round(percentage)

    if rounded_percentage >= 99:
        return "F"

    elif rounded_percentage <= 1:
        return "E"
    else:
        return rounded_percentage

main()
