from .code_772 import *
from .code_772 import remove_length


def test():
    assert remove_length('The person is most value tet', 3) == 'person is most value'