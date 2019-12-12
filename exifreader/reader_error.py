__autor__ = "Julian Huch"
__version__ = "1.0"


class BaseError(Exception):
    """ Base class for exceptions in this module. """
    def __repr__(self):
        return f"{self.__class__.__name__!r}"


class NoExifError(BaseError):
    """ Raised when no exif data available. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"NoExifError: {self.value!r}"
    def __str__(self):
        return self.__repr__()


class WebsiteDownError(BaseError):
    """ Raised when website is invalid. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"WebsiteDownError: {self.value!r}"
    def __str__(self):
        return self.__repr__()


class NoImageError(BaseError):
    """ Raised when there are no images on website. """
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"NoImageError: {self.value!r}"
    def __str__(self):
        return self.__repr__()
