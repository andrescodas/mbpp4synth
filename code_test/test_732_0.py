from .code_732 import *
from .code_732 import replace_specialchar


def test():
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')