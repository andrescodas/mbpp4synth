from .code_705 import *
from .code_705 import sort_sublists


def test():
    assert sort_sublists([["python"],["java","C","C++"],["DBMS"],["SQL","HTML"]])==[['DBMS'], ['python'], ['SQL', 'HTML'], ['java', 'C', 'C++']]