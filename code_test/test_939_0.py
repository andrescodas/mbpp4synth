from .code_939 import *
from .code_939 import sorted_models


def test():
    assert sorted_models([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}])==[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]