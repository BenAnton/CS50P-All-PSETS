months = [
    "January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

def main():
    date = take_check_input()
    words_or_numbers(date)


def take_check_input():
    while True:
        try:
            user_input = input("Please enter a date in either: M/D/YEAR or September 8, 1636 format: ")
            user_input = user_input.strip()
            if "/" in user_input:
                a, b, c = user_input.split("/")
                if a.isdigit():
                    return user_input

            elif "/" in user_input or "," in user_input:
                return user_input

            else:
                user_input = take_check_input()
        except ValueError:
            print("Invalid Format")


def words_or_numbers(date):
    for i in range(len(months)):
        if months[i] in date:
            months_index = i + 1
            convert_words_output(date, months_index)
            return
    convert_numbers_output(date)


def convert_words_output(date, months_index):
    month, day, year = date.split(" ")
    day = day.replace(",", "")
    if  month.isdigit():
        date = take_check_input()
    if int(day) > 31:
        date = take_check_input()
    if len(day) == 1:
        day = "0" + day
    month = str(months_index)
    if int(month) > 12:
        date = take_check_input()
    if len(month) == 1:
        month = "0" + month
    print(year + "-" + month + "-" + day)


def convert_numbers_output(date):
    month, day, year = date.split("/")
    if int(month) > 12:
        date = take_check_input()
    if not month.isdigit():
        date = take_check_input()
    if len(month) == 1:
        month = "0" + month
    if int(day) > 31:
        date = take_check_input()
    if len(day) == 1:
            day = "0" + day
    print(year + "-" + month + "-" + day)


main()
