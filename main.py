__autor__ = "Julian Huch"
__version__ = "1.0"


import sys
from exifreader import ImageHandler


class Main():
    """ Main Class """

    menu_txt = """
    EXIFREADER by Julian Huch
    A wrapper for Python's exif / exifread module

    [1] Download Pictures from URL
    [2] Read exif from file
    [0] Exit
    """

    @classmethod
    def run(cls):

        print(cls.menu_txt)
        choice = input("Choice > ")

        if choice == 1:
            image_url = input("Image URL > ")
            ImageHandler.download_images_from_html(image_url)

        elif choice == 2:
            image_file = input("Image file > ") 
            ImageHandler.print_exif_from_files(image_file)

        elif choice == 0:
            sys.exit(0)

        else:
            Main.run()


if __name__ == "__main__":
    Main.run()
