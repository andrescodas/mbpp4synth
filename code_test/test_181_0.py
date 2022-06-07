from .code_181 import *
from .code_181 import common_prefix


def test():
    assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'