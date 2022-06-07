from .code_73 import *
from .code_73 import multiple_split


def test():
    assert multiple_split('Certain services\nare subjected to change*over the seperate subscriptions.') == ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']