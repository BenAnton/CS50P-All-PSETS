variable = input("Please enter a variable in Camel Case: ")

def camel_to_snake(variable):
    snake_case = ""

    for char in variable:
        if char.isupper():
                snake_case += "_"
                snake_case += char.lower()
        else:
            snake_case += char
    print(snake_case)
    return snake_case

camel_to_snake(variable)
