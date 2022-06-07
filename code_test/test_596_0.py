from .code_596 import *
from .code_596 import tuple_size


def test():
    assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))