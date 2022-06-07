from .code_898 import *
from .code_898 import extract_elements


def test():
    assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]