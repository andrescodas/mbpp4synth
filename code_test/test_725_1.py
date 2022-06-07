from .code_725 import *
from .code_725 import extract_quotation


def test():
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']