import os
import shutil
import pytest
import flinch.os

def test_listpath():
    flinch.os.list_paths(".")
    assert len(flinch.os.list_paths(".")) >= 0, "current dir files is zeros"
