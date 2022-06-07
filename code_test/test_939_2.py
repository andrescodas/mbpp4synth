from .code_939 import *
from .code_939 import sorted_models


def test():
    assert sorted_models([{'make':'micromax','model':40,'color':'grey'},{'make':'poco','model':60,'color':'blue'}])==([{'make':'poco','model':60,'color':'blue'},{'make':'micromax','model':40,'color':'grey'}])