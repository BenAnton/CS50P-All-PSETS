import re


def main():
    s = input("HTML: ").strip()
    short_url = parse(s)
    print(short_url)


def parse(s):
    if matches := re.search(
        r"src=\"(?:https?://)?(?:www\.)?youtube\.com/embed/([\w]{11})", s, re.IGNORECASE
    ):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
