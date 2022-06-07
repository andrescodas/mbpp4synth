from .code_251 import *
from .code_251 import insert_element


def test():
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black'] 