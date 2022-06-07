from .code_156 import *
from .code_156 import tuple_int_str


def test():
    assert tuple_int_str((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))