from .code_213 import *
from .code_213 import concatenate_strings


def test():
    assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')