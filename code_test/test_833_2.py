from .code_833 import *
from .code_833 import get_key


def test():
    assert get_key({27:'language',39:'java',44:'little'})==[27,39,44]