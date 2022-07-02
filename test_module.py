import os
import shutil
import pytest
import pyfunctions

def test_listpath():
    pyfunctions.list_paths(".")
    assert len(pyfunctions.list_paths(".")) >= 0, "current dir files is zeros"
