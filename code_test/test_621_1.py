from .code_621 import *
from .code_621 import increment_numerics


def test():
    assert increment_numerics(["Dart", "356", "is", "88", "169", "Super", "6"] , 12) == ['Dart', '368', 'is', '100', '181', 'Super', '18']