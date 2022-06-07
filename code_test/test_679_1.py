from .code_679 import *
from .code_679 import access_key


def test():
    assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'