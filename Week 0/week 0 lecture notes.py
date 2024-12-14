# ask user for name and store in variable called name
#    name = input("What is your name?")

# remove all whitespace from start and end of string (not the middle)
#    name = name.strip()

# capitalise first letter of string
#    name = name.capitalize()

# first letter of each word in string
 #   name = name.title()

# chain functions
 #   name = name.strip().title()

# can also chain further:
  #  name = input("What is your name?").strip().title()

# splitting a string
#    first, last = name.split(" ")
 #   print(f"hello, {first}")

# print hello, name to console
  #  print("hello " + name)

# can keep mutliple print statements on one line
#    print("hello, ", end="")
#    print(name)

# to print a quotation mark
 #   print('hello, "friend"')
# or
 #   print("hello, \"friend\"")

# printing variable option
 #   print(f"hello, {name}")

# integers ==============================================

# mini calculator for addition
#    x = int(input("what is x? "))
#    y = int(input("what is y? "))
#    print(x + y)

# floats
#   x = float(input("what is x? "))
#   y = float(input("what is y? "))

#   z= round(x + y)
#   print(z)

# commas for large numbers
#   num = 1000
# print(f"{num:,}")

# functions ====================================
def hello(to="world"):
    print("Hello, " + to)
hello()
name = input("what is your name?")
hello(name)

