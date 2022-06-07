from .code_403 import *
from .code_403 import is_valid_URL


def test():
    assert is_valid_URL("https:// www.redit.com") == False