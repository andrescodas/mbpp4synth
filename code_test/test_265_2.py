from .code_265 import *
from .code_265 import list_split


def test():
    assert list_split(['python','java','C','C++','DBMS','SQL'],2)==[['python', 'C', 'DBMS'], ['java', 'C++', 'SQL']] 