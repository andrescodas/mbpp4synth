from .code_642 import *
from .code_642 import remove_similar_row


def test():
    assert remove_similar_row([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]] ) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}