from .code_272 import *
from .code_272 import rear_extract


def test():
    assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]