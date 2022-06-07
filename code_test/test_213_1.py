from .code_213 import *
from .code_213 import concatenate_strings


def test():
    assert concatenate_strings(("Shaik", "Ayesha", "Sanya"), (" Dawood", " Begum", " Singh")) == ('Shaik Dawood', 'Ayesha Begum', 'Sanya Singh')