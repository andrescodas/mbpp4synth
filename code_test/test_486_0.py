from .code_486 import *
from .code_486 import binomial_probability


def test():
    assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185