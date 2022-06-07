from .code_13 import *
from .code_13 import count_common


def test():
    assert count_common(['red','green','black','pink','black','white','black','eyes','white','black','orange','pink','pink','red','red','white','orange','white',"black",'pink','green','green','pink','green','pink','white','orange',"orange",'red']) == [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]