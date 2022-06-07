from .code_450 import *
from .code_450 import extract_string


def test():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']