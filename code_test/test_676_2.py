from .code_676 import *
from .code_676 import remove_extra_char


def test():
    assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'