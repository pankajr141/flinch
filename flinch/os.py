from asyncio import exceptions
from msilib import Directory
import os
from os import walk

def list_paths(dirpath):
    """ This function returns all filepaths present in current directory
    **Parameters**
    dirpath :  str
        directory path,
     **Returns**
    object
        all filepaths present in current directory
    """
    if not os.path.exists(dirpath):
        raise Exception("{} not present or valid".format(dirpath))

    return [os.path.join(dirpath, x) for x in os.listdir(dirpath)]

def list_paths_recursive(dirpath):
    """ This function returns all filepaths present in current and nested directory
    **Parameters**
    dirpath :  str
        directory path,
     **Returns**
    object
        all filepaths present in current and nested directory
    """
    if not os.path.exists(dirpath):
        raise Exception("{} not present or valid".format(dirpath))

    filepaths = []
    for root, directory, files in os.walk(dirpath):
        for file_ in files:
            filepaths.append(os.path.join(root, file_))

    filepaths = [x for x in filepaths]
    return filepaths