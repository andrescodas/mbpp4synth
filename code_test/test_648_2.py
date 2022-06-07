from .code_648 import *
from .code_648 import exchange_elements


def test():
    assert exchange_elements([25,35,45,55,75,95])==[35,25,55,45,95,75] 