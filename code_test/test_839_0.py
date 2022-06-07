from .code_839 import *
from .code_839 import sort_tuple


def test():
    assert sort_tuple([("Amana", 28), ("Zenat", 30), ("Abhishek", 29),("Nikhil", 21), ("B", "C")]) == [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]