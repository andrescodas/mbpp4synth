from .code_64 import *
from .code_64 import subject_marks


def test():
    assert subject_marks([('Physics',96),('Chemistry',97),('Biology',45)])==([('Biology',45),('Physics',96),('Chemistry',97)])