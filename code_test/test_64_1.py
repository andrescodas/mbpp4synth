from .code_64 import *
from .code_64 import subject_marks


def test():
    assert subject_marks([('Telugu',49),('Hindhi',54),('Social',33)])==([('Social',33),('Telugu',49),('Hindhi',54)])