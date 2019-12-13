__autor__ = "Julian Huch"
__version__ = "1.0"


from colorama import Fore, Style


class BaseError(Exception):
    """ Base class for exceptions in this module. """
    def __repr__(self):
        return f"{self.__class__.__name__!r}"


class NoExifError(BaseError):
    """ Raised when no exif data available. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return Fore.RED + f"NoExifError: {self.value!r}" + Style.RESET_ALL
    def __str__(self):
        return self.__repr__()


class WebsiteDownError(BaseError):
    """ Raised when website is invalid. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return Fore.RED + f"WebsiteDownError: {self.value!r}" + Style.RESET_ALL
    def __str__(self):
        return self.__repr__()


class NoImageError(BaseError):
    """ Raised when there are no images on website. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return Fore.RED + f"NoImageError: {self.value!r}" + Style.RESET_ALL
    def __str__(self):
        return self.__repr__()


class FileNotFoundError(BaseError):
    """ Raised when the file or directory didn't exist. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return Fore.RED + f"No such file or directory: {self.value!r}" + Style.RESET_ALL
    def __str__(self):
        return self.__repr__()
