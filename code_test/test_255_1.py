from .code_255 import *
from .code_255 import combinations_colors


def test():
    assert combinations_colors( ["Red","Green","Blue"],2)==[('Red', 'Red'), ('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Green'), ('Green', 'Blue'), ('Blue', 'Blue')]