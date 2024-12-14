import re
import sys


def main():
    ip = input("IP: ")
    validation = validate(ip)
    print(validation)


def validate(ip):
    pattern = r"^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$"
    try:

        if re.search(pattern, ip):
            return True
        if not re.search(pattern, ip):
             return False
    except ValueError:
         sys.exit(1)


if __name__ == "__main__":
        main()
