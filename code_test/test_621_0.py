from .code_621 import *
from .code_621 import increment_numerics


def test():
    assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"] , 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']