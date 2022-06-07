from .code_298 import *
from .code_298 import intersection_nested_lists


def test():
    assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]