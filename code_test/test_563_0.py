from .code_563 import *
from .code_563 import extract_values


def test():
    assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']