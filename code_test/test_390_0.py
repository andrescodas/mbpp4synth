from .code_390 import *
from .code_390 import add_string


def test():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']