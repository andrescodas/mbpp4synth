from .code_898 import *
from .code_898 import extract_elements


def test():
    assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]