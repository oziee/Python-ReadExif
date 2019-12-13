__autor__ = "Julian Huch"
__version__ = "1.0"


from exifreader import sys
from exifreader import os
from exifreader import ImageHandler
from exifreader import HandleFile


class BaseMain(object):

    menu_txt = """
    EXIFREADER by Julian Huch
    A wrapper for Python's exif / exifread module

    [1] Download Pictures from URL
    [2] Read exif from file
    [3] Read exif from directory files
    [0] Exit
    """


class Main(BaseMain):
    """ Main Class """

    def run(self):

        print(self.menu_txt)
        choice = input("Choice > ")

        if choice == "1":
            image_url = input("Image URL > ")
            ImageHandler.download_images_from_html(image_url)

        elif choice == "2":
            image_file = input("Image file > ").split()
            ImageHandler.print_exif_from_files(image_file)
        
        elif choice == "3":
            image_dir = input("Image dir > ")
            ImageHandler.print_exif_from_files(HandleFile.getListOfFiles(image_dir))
            
        elif choice == "0":
            sys.exit(0)
        
        else:
            self.run()


if __name__ == "__main__":
    app = Main()
    app.run()
