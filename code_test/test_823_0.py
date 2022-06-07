from .code_823 import *
from .code_823 import check_substring


def test():
    assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'