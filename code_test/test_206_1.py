from .code_206 import *
from .code_206 import concatenate_elements


def test():
    assert concatenate_elements(("RES ", "IS ", "BEST ", "FOR ", "ALL ", "QESR")) == ('RES IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL QESR')