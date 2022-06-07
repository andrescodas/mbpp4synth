from .code_821 import *
from .code_821 import merge_dictionaries


def test():
    assert merge_dictionaries({ "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'W': 'White', 'O': 'Orange', 'G': 'Green', 'B': 'Black'}