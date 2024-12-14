def main():
    time = input("Please enter a time: ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return float(hours + minutes / 60)


if __name__ == "__main__":
    main()
