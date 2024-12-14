math = input("please enter a sum: ")
math = math.split(" ")
x = float(math[0])
y = math[1]
z = float(math[2])

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
