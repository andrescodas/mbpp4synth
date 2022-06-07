from .code_427 import *
from .code_427 import change_date_format


def test():
    assert change_date_format("2021-04-26") == '26-04-2021'