__autor__ = "Julian Huch"
__versin__ = "1.0"


import os
import exif
import exifread
from collections import defaultdict
import requests
import urllib
from bs4 import BeautifulSoup


from exifreader.reader_error import NoExifError, WebsiteDownError, NoImageError


class BaseImageHandler(object):
    """ Base Class for handle images. """

    def __repr__(self):
        return f"{self.__class__.__name__!r}"
    def print_exif_from_files(self):
        pass
    def return_exiflist_from_files(self):
        pass
    def mod_exif_in_file(self):
        pass
    def download_images_from_html(self):
        pass


class ImageHandler(BaseImageHandler):
    """ Image Handler class, contains some static methods for handling exif data """

    def __repr__(self):
        return f"{self.__class__.__name__!r}"

    @staticmethod
    def print_exif_from_files(*args):
        
        for image_file in args:

            try:
                # Check if the file exists, otherwise raise FileNotFoundError.
                if not os.path.isfile(image_file):
                    raise FileNotFoundError(image_file)
                
                # Open the file, check if there are exif data, otherwise raise NoExifError.
                with open(image_file, "rb") as f:
                    if exif.Image(f).has_exif:
                        tags = exifread.process_file(f)     # this returns a dictionary contains exif data.
                        for key, value in tags.items():
                            print(image_file)
                            print(f"{key}: {value}")        # print the exif data from the dictionary.
                    else:
                        raise NoExifError(image_file)
            
            except FileNotFoundError as ex:
                print(ex)
            except NoExifError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
    
    @staticmethod
    def return_exiflist_from_files(*args):

        mret = []

        for image_file in args:

            try:
                # Check if the file exists, otherwise raise FileNotFoundError.
                if not os.path.isfile(image_file):
                    raise FileNotFoundError(image_file)
                
                # Open the file, check if there are exif data, otherwise raise NoExifError.
                with open(image_file, "rb") as f:
                    if exif.Image(f).has_exif:
                        mret.append(exifread.process_file(f))    # adds dictionary to mret list.
                    else:
                        raise NoExifError(image_file)
            
            except FileNotFoundError as ex:
                print(ex)
            except NoExifError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
        
        return mret     # returns list with dictionay who contains exif data
    
    @staticmethod
    def mod_exif_from_file(image_file):
        pass
    
    @staticmethod
    def download_images_from_html(image_url):
        try:
            response = requests.get(image_url)

            # Check if the site's up, otherwise raise WebsiteDownError.
            if response.status_code == 200:

                soup = BeautifulSoup(response.text, "html.parser")      # Parse html code from website
                images = soup.find_all("img")                           # Filter image tag out of parsed html code

                # Check if there are images and create a directory, otherwise raise NoImageError.
                if images:
                    image_dir = "".join([c if c.isalpha() else "_" for c in image_url])
                    if not os.path.isdir(image_dir):
                        os.mkdir(image_dir)
                else:
                    raise NoImageError(image_url)
                
                # Make list of full urls's from found images in given image_url.
                found_images = [urllib.parse.urljoin(image_url, img.attrs["src"]) for img in images]
                
                # Download images
                image_count = 0
                for found_image in found_images:
                    filename = found_image.split("/")[-1]
                    response_image = requests.get(found_image)
                    with open(image_dir + "/" + filename, "wb") as file:
                        image_count += 1
                        file.write(response_image.content)
                        print(f"Saved Image: [{filename} to: [{image_dir}]")
                print(f"Download Complete: We found and save [{image_count}] images at [{image_dir}]")

            else:
                raise WebsiteDownError(response.status_code)
        
        except WebsiteDownError as ex:
            print(ex)
        except NoImageError as ex:
            print(ex)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    """ This is just for debugging. """
    image_file = input("Image file > ")
    handler = ImageHandler()
    handler.print_exif_from_files(image_file)
