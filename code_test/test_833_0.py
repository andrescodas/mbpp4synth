from .code_833 import *
from .code_833 import get_key


def test():
    assert get_key({1:'python',2:'java'})==[1,2]