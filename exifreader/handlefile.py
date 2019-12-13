__autor__ = "Julian Huch"
__version__ = "1.0"


from exifreader import sys
from exifreader import os
from exifreader import ABCMeta, abstractmethod
from exifreader import FileNotFoundError


class BaseHandleFile(metaclass=ABCMeta):

    @abstractmethod
    def getListOfFiles(self):
        pass


class HandleFile(BaseHandleFile):

    @staticmethod
    def getListOfFiles(dirName):

        allFiles = []

        try:
            if not os.path.isdir(dirName):
                raise FileNotFoundError(dirName)
            
            for file_name in os.listdir(dirName):
                fullpath = os.path.join(dirName, file_name)
                if not os.path.isdir(fullpath):
                    allFiles.append(fullpath)
        
        except FileNotFoundError as ex:
            print(ex)
            sys.exit(1)
        except Exception as ex:
            print(ex)
            sys.exit(1)
        
        else:
            return allFiles
