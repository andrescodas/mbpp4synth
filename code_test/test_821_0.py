from .code_821 import *
from .code_821 import merge_dictionaries


def test():
    assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}