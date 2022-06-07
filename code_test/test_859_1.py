from .code_859 import *
from .code_859 import sub_lists


def test():
    assert sub_lists(['X', 'Y', 'Z'])==[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]