from .code_411 import *
from .code_411 import snake_to_camel


def test():
    assert snake_to_camel('google_pixel') == 'GooglePixel'