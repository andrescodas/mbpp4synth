from .code_475 import *
from .code_475 import sort_counter


def test():
    assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87})==[('Chemistry', 87), ('Physics', 83), ('Math', 81)]