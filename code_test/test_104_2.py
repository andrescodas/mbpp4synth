from .code_104 import *
from .code_104 import sort_sublists


def test():
    assert sort_sublists((["zilver","gold"], ["magnesium","aluminium"], ["steel", "bronze"]))==[['gold', 'zilver'],['aluminium', 'magnesium'], ['bronze', 'steel']]