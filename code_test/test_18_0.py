from .code_18 import *
from .code_18 import remove_dirty_chars


def test():
    assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'