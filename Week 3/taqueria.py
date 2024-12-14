items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total = 0.0

    print("Select Menu Item, when done press ctrl+d: ")

    while True:
        try:
            user_prompt = input("Menu Item: ")
            user_prompt = user_prompt.title()
            if (user_prompt) in items:
                total +=  items[user_prompt]
                total = round(total, 2)
                print(f"Total: ${total:.2f}")
            else:
                print("Invalid Item")
               
        except EOFError:
            print("Error Occured")
            break



main()

