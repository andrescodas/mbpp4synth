from .code_220 import *
from .code_220 import replace_max_specialchar


def test():
    assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')