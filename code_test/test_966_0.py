from .code_966 import *
from .code_966 import remove_empty


def test():
    assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  