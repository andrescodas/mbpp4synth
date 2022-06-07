from .code_427 import *
from .code_427 import change_date_format


def test():
    assert change_date_format("2020-11-13") == '13-11-2020'