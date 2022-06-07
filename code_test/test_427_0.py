from .code_427 import *
from .code_427 import change_date_format


def test():
    assert change_date_format("2026-01-02") == '02-01-2026'