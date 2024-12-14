import inflect


def main():
    name_list = get_name()
    create_string(name_list)


def get_name():
    name_list = []
    while True:
        try:
            name_input = input()
            name_list.append(name_input)
        except EOFError:
            return name_list


def create_string(name_list):

    part1 = "Adieu, adieu, to "
    part2 = ""

    if len(name_list) == 1:
        part2 = name_list[0]
    elif len(name_list) == 2:
        part2 = ", ".join(name_list[:-1]) + " and " + name_list[-1]
    else:
        part2 = ", ".join(name_list[:-1]) + ", and " + name_list[-1]

    print(part1 + part2)


main()
