from .code_823 import *
from .code_823 import check_substring


def test():
    assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'