from .code_206 import *
from .code_206 import concatenate_elements


def test():
    assert concatenate_elements(("MSAM", "IS ", "BEST ", "FOR ", "ALL ", "SKD")) == ('MSAMIS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL SKD')