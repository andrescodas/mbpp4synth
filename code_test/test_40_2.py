from .code_40 import *
from .code_40 import freq_element


def test():
    assert freq_element([[15,20,30,40],[80,90,100,110],[30,30,80,90]])==({30: 3, 80: 2, 90: 2, 15: 1, 20: 1, 40: 1, 100: 1, 110: 1})