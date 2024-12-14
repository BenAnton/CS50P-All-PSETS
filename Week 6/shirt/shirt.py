from PIL import Image, ImageOps
import sys

waste, inputExt = sys.argv[1].rsplit(".")
print(inputExt)
waste, outputExt = sys.argv[2].rsplit(".")
print(outputExt)
shirt = Image.open("shirt.png")
size = shirt.size


def main():
    if len(sys.argv) != 3:
        sys.exit("CLI length wrong")

    if not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[
        2
    ].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid Ext")

    if inputExt != outputExt:
        sys.exit("filenames do not match")

    with Image.open(sys.argv[1]) as image:
        resize = ImageOps.fit(image, size)
        resize.paste(shirt, shirt)
        resize.save(sys.argv[2])


main()
