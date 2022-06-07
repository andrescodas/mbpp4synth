from .code_725 import *
from .code_725 import extract_quotation


def test():
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']