from PIL import Image
import os

path = "C://Users//qakashi//Desktop//drlngstickers"
new_path = "C://Users//qakashi//Desktop//formatted//"
line_separator = "//"


def main():
    for x in os.listdir(path):
        if x.endswith(".jpg"):
            image = Image.open(path + line_separator + x)
            image.thumbnail((512, 512))
            image.save(new_path + x.rsplit('.', maxsplit=1)[0] + ".png")


if __name__ == '__main__':
    main()
