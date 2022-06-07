from .code_156 import *
from .code_156 import tuple_int_str


def test():
    assert tuple_int_str((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))