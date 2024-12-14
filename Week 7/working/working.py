import re
import sys


def main():
    print(convert(input("Hours: ")))



def convert(s):
    matches = re.search(
        r"(\d\d?)(:(\d\d))? ([ap]m) to (\d\d?)(:(\d\d))? ([ap]m)", s, re.IGNORECASE
    )

    if matches:
        h1 = int(matches.group(1))
        m1 = matches.group(3) if matches.group(3) else "00"
        period1 = matches.group(4).lower()

        h2 = int(matches.group(5))
        m2 = matches.group(7) if matches.group(7) else "00"
        period2 = matches.group(8).lower()

        if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
            raise ValueError
        if not (0 <= int(m1) < 60 and 0 <= int(m2) < 60):
            raise ValueError

        h1 = convert_24(h1, period1)
        h2 = convert_24(h2, period2)

        return f"{h1:02}:{m1} to {h2:02}:{m2}"

    raise ValueError


def convert_24(hour, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    return hour


if __name__ == "__main__":
    main()
