from .code_104 import *
from .code_104 import sort_sublists


def test():
    assert sort_sublists(([" red ","green" ],["blue "," black"],[" orange","brown"]))==[[' red ', 'green'], [' black', 'blue '], [' orange', 'brown']]