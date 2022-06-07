from .code_173 import *
from .code_173 import remove_splchar


def test():
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')