from .code_906 import *
from .code_906 import extract_date


def test():
    assert extract_date("https://www.indiatoday.in/movies/celebrities/story/wp/2020/11/03/odeof-sushant-singh-rajput-s-death-his-brother-in-law-shares-advice-for-fans-1749646/") == [('2020', '11', '03')]