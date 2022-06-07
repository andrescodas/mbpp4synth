from .code_932 import *
from .code_932 import remove_duplic_list


def test():
    assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","C++","C","C++"])==['Python', 'Exercises', 'Practice', 'Solution','C++','C']