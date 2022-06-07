from .code_156 import *
from .code_156 import tuple_int_str


def test():
    assert tuple_int_str((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))