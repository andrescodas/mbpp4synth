from .code_857 import *
from .code_857 import listify_list


def test():
    assert listify_list([' red ', 'green',' black', 'blue ',' orange', 'brown'])==[[' ', 'r', 'e', 'd', ' '], ['g', 'r', 'e', 'e', 'n'], [' ', 'b', 'l', 'a', 'c', 'k'], ['b', 'l', 'u', 'e', ' '], [' ', 'o', 'r', 'a', 'n', 'g', 'e'], ['b', 'r', 'o', 'w', 'n']]