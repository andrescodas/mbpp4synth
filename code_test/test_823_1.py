from .code_823 import *
from .code_823 import check_substring


def test():
    assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'