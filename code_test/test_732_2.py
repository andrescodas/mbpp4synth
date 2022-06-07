from .code_732 import *
from .code_732 import replace_specialchar


def test():
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')