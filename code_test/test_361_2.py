from .code_361 import *
from .code_361 import remove_empty


def test():
    assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']