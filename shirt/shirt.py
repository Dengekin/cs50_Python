import sys
from PIL import Image, ImageOps
import os

def main():
    arg_count = len(sys.argv)
    if arg_count < 3:
        sys.exit("Too few command-line arguments")
    if arg_count > 3:
        sys.exit("Too many command-line arguments")

    shirtpath = sys.argv[1]
    muppetpath = sys.argv[2]

    valid_end = {".jpg",".jpeg",".png"}
    in_end    = os.path.splitext(input_path)[1]
    out_end   = os.path.splitext(output_path)[1]

    if in_end not in valid_end:
        sys.exit("Invalid input")
    if out_end not in valid_end:
        sys.exit("Invalid output")
    if in_end != out_end:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(shirtpath)
        
        fitted = ImageOps.fit(photo, shirt.size)
        fitted.paste(shirt,shirt)
        fitted.save(muppetpath)
    except FileNotFoundError:
        sys.exit("Input does not exist")

main()
