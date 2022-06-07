from .code_829 import *
from .code_829 import second_frequent


def test():
    assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'