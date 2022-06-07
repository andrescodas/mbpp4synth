from .code_643 import *
from .code_643 import text_match_wordz_middle


def test():
    assert text_match_wordz_middle("  lang  .")==('Not matched!')