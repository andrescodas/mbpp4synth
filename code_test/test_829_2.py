from .code_829 import *
from .code_829 import second_frequent


def test():
    assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'