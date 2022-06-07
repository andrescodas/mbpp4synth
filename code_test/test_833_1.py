from .code_833 import *
from .code_833 import get_key


def test():
    assert get_key({10:'red',20:'blue',30:'black'})==[10,20,30]