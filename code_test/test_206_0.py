from .code_206 import *
from .code_206 import concatenate_elements


def test():
    assert concatenate_elements(("DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS")) == ('DSP IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL UTS')