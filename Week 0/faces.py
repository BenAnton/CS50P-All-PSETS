def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    print(string)

def main():
    userInput = input("")
    convert(userInput)



main()

