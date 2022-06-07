from .code_725 import *
from .code_725 import extract_quotation


def test():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']