from .code_795 import *
from .code_795 import cheap_items


def test():
    assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]