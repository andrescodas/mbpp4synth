from .code_771 import *
from .code_771 import check_expression


def test():
    assert check_expression("{()}[{]") == False