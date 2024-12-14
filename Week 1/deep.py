question = input("What is the meaning of life? ")
question = question.lower().strip()

if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes")
else:
    print("No")
