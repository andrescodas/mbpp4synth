from .code_857 import *
from .code_857 import listify_list


def test():
    assert listify_list(['Red', 'Blue', 'Black', 'White', 'Pink'])==[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]