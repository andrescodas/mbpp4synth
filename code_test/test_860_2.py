from .code_860 import *
from .code_860 import check_alphanumeric


def test():
    assert check_alphanumeric("cooltricks@") == 'Discard'