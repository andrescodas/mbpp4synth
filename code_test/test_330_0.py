from .code_330 import *
from .code_330 import find_char


def test():
    assert find_char('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']