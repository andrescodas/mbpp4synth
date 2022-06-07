from .code_475 import *
from .code_475 import sort_counter


def test():
    assert sort_counter({'Math':400, 'Physics':300, 'Chemistry':250})==[('Math', 400), ('Physics', 300), ('Chemistry', 250)]