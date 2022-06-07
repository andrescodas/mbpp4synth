from .code_642 import *
from .code_642 import remove_similar_row


def test():
    assert remove_similar_row([[(6, 7), (5, 4)], [(4, 4), (6, 8)], [(5, 4), (6, 7)]] ) =={((4, 4), (6, 8)), ((5, 4), (6, 7))}