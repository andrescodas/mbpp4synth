from .code_391 import *
from .code_391 import convert_list_dictionary


def test():
    assert convert_list_dictionary(["A1","A2","A3","A4"],["java","C","C++","DBMS"],[10,20,30,40])==[{'A1':{'java':10}},{'A2':{'C':20}},{'A3':{'C++':30}},{'A4':{'DBMS':40}}]