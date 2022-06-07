from .code_906 import *
from .code_906 import extract_date


def test():
    assert extract_date("https://economictimes.indiatimes.com/news/economy/2020/12/29/finance/pension-assets-under-pfrda-touch-rs-5-32-lakh-crore/articleshow/79736619.cms") == [('2020', '12', '29')]