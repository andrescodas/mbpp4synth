from .code_475 import *
from .code_475 import sort_counter


def test():
    assert sort_counter({'Math':900, 'Physics':1000, 'Chemistry':1250})==[('Chemistry', 1250), ('Physics', 1000), ('Math', 900)]