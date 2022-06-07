from .code_37 import *
from .code_37 import sort_mixed_list


def test():
    assert sort_mixed_list([19,'red',12,'green','blue', 10,'white','green',1])==[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']