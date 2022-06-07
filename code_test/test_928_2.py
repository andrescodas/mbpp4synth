from .code_928 import *
from .code_928 import change_date_format


def test():
    assert change_date_format('2030-06-06')=='06-06-2030'