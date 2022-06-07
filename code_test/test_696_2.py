from .code_696 import *
from .code_696 import zip_list


def test():
    assert zip_list([['a','b'],['c','d']] , [['e','f'],['g','h']] )==[['a','b','e','f'],['c','d','g','h']]