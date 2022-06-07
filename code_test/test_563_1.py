from .code_563 import *
from .code_563 import extract_values


def test():
    assert extract_values('"python","program","language"')==['python','program','language']