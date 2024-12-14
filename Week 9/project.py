def main():
    user_input = input(
        "What type would you like to convert? options: Length, Weight, Area, Time, Temperature \n"
    ).lower()
    result = convert_what(user_input)
    print(result)


def convert_what(user_input):

    if user_input == "length":
        return length()
    if user_input == "weight":
        return weight()
    if user_input == "area":
        return area()
    if user_input == "time":
        return time()
    if user_input == "temperature":
        return temperature()
    else:
        raise ValueError("Invalid Input")


def length():
    convert_from = input(
        "Please enter what you would like to convert from? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    convert_to = input(
        "Please enter what you would like to convert to? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    amount = int(input("What is the amount as an integer?\n"))
    return convert_length(convert_from, convert_to, amount)


def convert_length(convert_from, convert_to, amount):
    if convert_from == "cm":
        if convert_to == "m":
            return amount / 100
        if convert_to == "miles":
            return amount / 160900
        if convert_to == "km":
            return amount / 100000
        if convert_to == "inch":
            return amount / 2.54
        if convert_to == "foot":
            return amount / 30.48

    if convert_from == "m":
        if convert_to == "cm":
            return amount * 100
        if convert_to == "miles":
            return amount / 1609.34
        if convert_to == "km":
            return amount / 1000
        if convert_to == "inch":
            return amount * 39.37
        if convert_to == "foot":
            return amount * 3.281

    if convert_from == "miles":
        if convert_to == "cm":
            return amount * 160900
        if convert_to == "m":
            return amount * 1609.34
        if convert_to == "km":
            return amount * 1.609
        if convert_to == "inch":
            return amount * 63360
        if convert_to == "foot":
            return amount * 5280

    if convert_from == "km":
        if convert_to == "cm":
            return amount * 100000
        if convert_to == "m":
            return amount * 100
        if convert_to == "miles":
            return amount / 1.609
        if convert_to == "inch":
            return amount * 39370
        if convert_to == "foot":
            return amount * 3281

    if convert_from == "inch":
        if convert_to == "cm":
            return amount * 2.54
        if convert_to == "m":
            return amount / 39.37
        if convert_to == "miles":
            return amount / 63360
        if convert_to == "km":
            return amount / 39370
        if convert_to == "foot":
            return amount / 12

    if convert_from == "foot":
        if convert_to == "cm":
            return amount * 30.48
        if convert_to == "m":
            return amount / 3.281
        if convert_to == "miles":
            return amount / 5280
        if convert_to == "km":
            return amount / 3281
        if convert_to == "inch":
            return amount * 12


def weight():
    convert_from = input(
        "Please enter what you would like to convert from? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    convert_to = input(
        "Please enter what you would like to convert to? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    amount = int(input("What is the amount as an integer?\n"))
    return convert_weight(convert_from, convert_to, amount)


def convert_weight(convert_from, convert_to, amount):
    if convert_from == "kg":
        if convert_to == "lbs":
            return amount * 2.205
        if convert_to == "stone":
            return amount / 6.35

    if convert_from == "lbs":
        if convert_to == "kg":
            return amount / 2.205
        if convert_to == "stone":
            return amount / 14

    if convert_from == "stone":
        if convert_to == "kg":
            return amount * 6.35
        if convert_to == "lbs":
            return amount * 14


def area():
    convert_from = input(
        "Please enter what you would like to convert from? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    convert_to = input(
        "Please enter what you would like to convert to? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    amount = int(input("What is the amount as an integer?\n"))
    return convert_area(convert_from, convert_to, amount)


def convert_area(convert_from, convert_to, amount):
    if convert_from == "miles":
        if convert_to == "metres":
            return amount * 2589989
        if convert_to == "acres":
            return amount * 640

    if convert_from == "metres":
        if convert_to == "miles":
            return amount / 1609.344
        if convert_to == "acres":
            return amount / 4047.86

    if convert_from == "acres":
        if convert_to == "miles":
            return amount / 640
        if convert_to == "metres":
            return amount * 4047.86


def time():
    convert_from = input(
        "Please enter what you would like to convert from? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    convert_to = input(
        "Please enter what you would like to convert to? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    amount = int(input("What is the amount as an integer?\n"))
    return convert_time(convert_from, convert_to, amount)


def convert_time(convert_from, convert_to, amount):
    if convert_from == "seconds":
        if convert_to == "minutes":
            return amount / 60
        if convert_to == "hours":
            return amount / 3600

    if convert_from == "minutes":
        if convert_to == "seconds":
            return amount * 60
        if convert_to == "hours":
            return amount / 60

    if convert_from == "hours":
        if convert_to == "seconds":
            return amount * 3600
        if convert_to == "minutes":
            return amount * 60


def temperature():
    convert_from = input(
        "Please enter what you would like to convert from? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    convert_to = input(
        "Please enter what you would like to convert to? options: CM, M, Miles, KM, Inch, Foot \n"
    ).lower()
    amount = int(input("What is the amount as an integer?\n"))
    return convert_temperature(convert_from, convert_to, amount)


def convert_temperature(convert_from, convert_to, amount):
    if convert_from == "c":
        if convert_to == "f":
            return (amount * 1.8) + 32
    if convert_from == "f":
        if convert_to == "c":
            return (amount - 32) / 1.8


if __name__ == "__main__":
    main()
