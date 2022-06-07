from .code_220 import *
from .code_220 import replace_max_specialchar


def test():
    assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')