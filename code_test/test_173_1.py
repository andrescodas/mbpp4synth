from .code_173 import *
from .code_173 import remove_splchar


def test():
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')