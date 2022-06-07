from .code_272 import *
from .code_272 import rear_extract


def test():
    assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]