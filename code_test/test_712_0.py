from .code_712 import *
from .code_712 import remove_duplicate


def test():
    assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 