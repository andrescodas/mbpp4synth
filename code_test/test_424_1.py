from .code_424 import *
from .code_424 import extract_rear


def test():
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']