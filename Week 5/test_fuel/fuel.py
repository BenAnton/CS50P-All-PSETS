def main():
    fraction = input("Please give a fraction in X/Y format: ")
    try:
        percentage = convert(fraction)
        output = gauge(percentage)
        print(output)
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("cannot divide by zero")

def convert(fraction):
    try:
        X, Y = map(int, fraction.split("/"))

        if Y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if  X > Y:
            raise ValueError("Numerator cannot be greater")

        percentage = (X / Y) * 100
        return percentage

    except ValueError:
        raise ValueError("Value Error")


def gauge(percentage):
    percentage = float(percentage)
    rounded_percentage = round(percentage)

    if rounded_percentage >= 99:
        return "F"

    elif rounded_percentage <= 1:
        return "E"
    else:
        return str(rounded_percentage)


if __name__ == "__main__":
    main()
