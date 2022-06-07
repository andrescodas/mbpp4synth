from .code_928 import *
from .code_928 import change_date_format


def test():
    assert change_date_format('2021-01-04')=='04-01-2021'