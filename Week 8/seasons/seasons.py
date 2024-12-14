from datetime import datetime, date
import sys
import re
import inflect

class Date_diff:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    def __sub__(self, other):
        birthdate = datetime(self.year, self.month, self.day)
        date = datetime(other.year, other.month, other.day)
        return (birthdate - date).days

    def __str__(self):
        return f"name={self.name} year={self.year}, month={self.month}, day={self.day}"


def main():
    birthdate = input("Enter birthday in YYYY-MM-DD format: ")
    birthday = get_birthdate(birthdate)
    today_date = get_today()
    days_difference = birthday - today_date
    minutes = convert_to_mins(days_difference)
    text = convert_to_text(minutes)
    print(f"{text} minutes")

def get_birthdate(birthdate):

        if matches := re.search(r"^(\d{4})-(\d\d)-(\d\d)$", birthdate):
            return Date_diff(name="birthday", year=matches.group(1), month=matches.group(2), day=matches.group(3))

        sys.exit(1)


def get_today():
    today_date = str(date.today())
    return Date_diff(name="today", year=today_date[0:4], month=today_date[5:7], day=today_date[8:10])

def convert_to_mins(days):
    days = days * -1
    return days * 24 * 60

def convert_to_text(mins):
    e = inflect.engine()
    written = e.number_to_words(mins)
    written = written.capitalize().replace(" and ", " ")
    return written

if __name__ == "__main__":
    main()
