from .code_500 import *
from .code_500 import concatenate_elements


def test():
    assert concatenate_elements([ 'Hi', 'there', 'How','are', 'you'] ) == '  Hi there How are you'