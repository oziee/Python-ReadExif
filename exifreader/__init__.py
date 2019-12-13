__autor__ = "Julian Huch"
__versin__ = "1.0"


""" Python Imports. """
from abc import ABCMeta, abstractmethod
import os
import sys
#import exif
import exifread
import requests
import urllib
from bs4 import BeautifulSoup
from colorama import Fore, Style


""" Module Imports. """
from exifreader.reader_error import NoExifError, WebsiteDownError, NoImageError, FileNotFoundError
from exifreader.imagehandler import ImageHandler
from exifreader.handlefile import HandleFile
