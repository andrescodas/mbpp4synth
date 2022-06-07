from .code_615 import *
from .code_615 import average_tuple


def test():
    assert average_tuple( ((100, 100, 100, 120), (300, 450, 560, 450), (810, 800, 390, 320), (10, 20, 30, 40)))==[305.0, 342.5, 270.0, 232.5]