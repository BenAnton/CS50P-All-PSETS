from pyfiglet import Figlet
import sys
import random

# figlet = Figlet()
# get list of fonts with:
# figlet.getFonts()
# set font with:
# figlet.setFont(font=f)
# output font in the text with:
# print(figlet.renderText(s))

figlet = Figlet()
fonts = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        output_random_font()
    elif len(sys.argv) == 3:
        check_cli()
    else:
        sys.exit(1)


def check_cli():
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            output_string_font()
        else:
            sys.exit(1)
    else:
        sys.exit(1)


def output_string_font():
    font = sys.argv[2]
    user_input = input("Enter String: ")
    figlet.setFont(font=font)
    print(figlet.renderText(user_input))


def output_random_font():
    user_input = input("Enter String: ")
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print(figlet.renderText(user_input))


main()
