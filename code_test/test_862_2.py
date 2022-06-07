from .code_862 import *
from .code_862 import n_common_words


def test():
    assert n_common_words("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]