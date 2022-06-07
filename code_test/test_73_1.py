from .code_73 import *
from .code_73 import multiple_split


def test():
    assert multiple_split('Mi Box runs on the \n Latest android*which has google assistance and chromecast.') == ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']