grocery_list = []

def main():
    get_item()

def end_of_file(grocery_list):
    grocery_list = sorted(grocery_list)
    count_items(grocery_list)

def get_item():
    while True:
        try:
            user_input = input()
            grocery_list.append(user_input)

        except EOFError:
            end_of_file(grocery_list)
            break

def count_items(items):
    item_counts = {}

    for item in items:
        item_upper = item.upper()
        if item_upper in item_counts:
            item_counts[item_upper] += 1
        else:
            item_counts[item_upper] = 1

    for item, count in item_counts.items():
        print(f"{count} {item}")
main()

