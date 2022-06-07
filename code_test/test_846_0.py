from .code_846 import *
from .code_846 import find_platform


def test():
    assert find_platform([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000],6)==3