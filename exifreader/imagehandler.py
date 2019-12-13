__autor__ = "Julian Huch"
__version__ = "1.0"


from exifreader import os
from exifreader import exifread
from exifreader import requests
from exifreader import urllib
from exifreader import BeautifulSoup
from exifreader import ABCMeta, abstractmethod
from exifreader import NoExifError, WebsiteDownError, FileNotFoundError, NoImageError


class BaseImageHandler(metaclass=ABCMeta):
    """ Base Class for handle images. """

    @abstractmethod
    def print_exif_from_files(self):
        pass

    @abstractmethod
    def return_exiflist_from_files(self):
        pass

    @abstractmethod 
    def mod_exif_in_file(self):
        pass

    @abstractmethod
    def download_images_from_html(self):
        pass


class ImageHandler(BaseImageHandler):
    """ Image Handler class, contains some static methods for handling exif data """

    def __repr__(self):
        return f"{self.__class__.__name__!r}"

    @staticmethod
    def print_exif_from_files(*args):
        """ This method directly prints the result to stdout. """
        
        for image_file in args:

            try:
                # Check if the file exists, otherwise raise FileNotFoundError.
                if not os.path.isfile(image_file):
                    raise FileNotFoundError(image_file)
                
                # Open the file, check if there are exif data, otherwise raise NoExifError.
                with open(image_file, "rb") as f:
                    tags = exifread.process_file(f, strict=True)     # this returns a dictionary contains exif data.
                    if not tags:
                        raise NoExifError(image_file)
                    print(f"Image: {image_file}")
                    for key, value in tags.items():
                        print(f"{key}: {value}")        # print the exif data from the dictionary.
            
            except FileNotFoundError as ex:
                print(ex)
            except NoExifError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
    
    @staticmethod
    def return_exiflist_from_files(*args):
        """ This method returns the found exif data in a list contains a dictionary for every given file. """

        exifDictionaryList = []

        for image_file in args:

            try:
                # Check if the file exists, otherwise raise FileNotFoundError.
                if not os.path.isfile(image_file):
                    raise FileNotFoundError(image_file)
                
                # Open the file, check if there are exif data, otherwise raise NoExifError.
                with open(image_file, "rb") as f:
                    tags = exifread.process_file(f, strict=True)
                    if not tags:
                        raise NoExifError(image_file)
                    exifDictionaryList.append([image_file, exifread.process_file(f)])    # adds dictionary to mret list.
            
            except FileNotFoundError as ex:
                print(ex)
            except NoExifError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
        
        return exifDictionaryList     # returns list with dictionay who contains exif data

    @staticmethod
    def mod_exif_in_file(image_file, *kwargs):
        """
        Here we implement the exif module for modify. 
        But it's not implemented actually.
        """

        print("Not implemented yet!")
    
    @staticmethod
    def download_images_from_html(image_url):
        """ Download method for simplyfing downloading images from every html page. """

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
    handler.mod_exif_in_file(image_file)
