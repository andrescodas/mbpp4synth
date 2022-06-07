from .code_933 import *
from .code_933 import camel_to_snake


def test():
    assert camel_to_snake('GoogleAssistant') == 'google_assistant'