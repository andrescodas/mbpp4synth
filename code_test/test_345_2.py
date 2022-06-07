from .code_345 import *
from .code_345 import diff_consecutivenums


def test():
    assert diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7])==[1, 1, 1, 1, 0, 0, 0, 1, 2]