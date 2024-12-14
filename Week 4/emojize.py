import emoji
import sys

try:
    user_input = input("Please enter an emoji string: ")
    emo = emoji.emojize(user_input, language="alias")
except:
    sys.exit()
print(emo)
