from .code_859 import *
from .code_859 import sub_lists


def test():
    assert sub_lists([1,2,3])==[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]