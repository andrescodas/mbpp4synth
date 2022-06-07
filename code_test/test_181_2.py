from .code_181 import *
from .code_181 import common_prefix


def test():
    assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'