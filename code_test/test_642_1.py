from .code_642 import *
from .code_642 import remove_similar_row


def test():
    assert remove_similar_row([[(5, 6), (4, 3)], [(3, 3), (5, 7)], [(4, 3), (5, 6)]] ) == {((4, 3), (5, 6)), ((3, 3), (5, 7))}