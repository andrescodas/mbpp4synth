from .code_493 import *
from .code_493 import calculate_polygons


def test():
    assert calculate_polygons(5,4,7,9,8)==[[(-11.0, -9.856406460551018), (-11.0, -0.6188021535170058), (-3.0, 4.0), (5.0, -0.6188021535170058), (5.0, -9.856406460551018), (-3.0, -14.475208614068023), (-11.0, -9.856406460551018)], [(5.0, -9.856406460551018), (5.0, -0.6188021535170058), (13.0, 4.0), (21.0, -0.6188021535170058), (21.0, -9.856406460551018), (13.0, -14.475208614068023), (5.0, -9.856406460551018)], [(21.0, -9.856406460551018), (21.0, -0.6188021535170058), (29.0, 4.0), (37.0, -0.6188021535170058), (37.0, -9.856406460551018), (29.0, -14.475208614068023), (21.0, -9.856406460551018)], [(-3.0, 4.0), (-3.0, 13.237604307034012), (5.0, 17.856406460551018), (13.0, 13.237604307034012), (13.0, 4.0), (5.0, -0.6188021535170058), (-3.0, 4.0)], [(13.0, 4.0), (13.0, 13.237604307034012), (21.0, 17.856406460551018), (29.0, 13.237604307034012), (29.0, 4.0), (21.0, -0.6188021535170058), (13.0, 4.0)], [(-11.0, 17.856406460551018), (-11.0, 27.09401076758503), (-3.0, 31.712812921102035), (5.0, 27.09401076758503), (5.0, 17.856406460551018), (-3.0, 13.237604307034012), (-11.0, 17.856406460551018)], [(5.0, 17.856406460551018), (5.0, 27.09401076758503), (13.0, 31.712812921102035), (21.0, 27.09401076758503), (21.0, 17.856406460551018), (13.0, 13.237604307034012), (5.0, 17.856406460551018)], [(21.0, 17.856406460551018), (21.0, 27.09401076758503), (29.0, 31.712812921102035), (37.0, 27.09401076758503), (37.0, 17.856406460551018), (29.0, 13.237604307034012), (21.0, 17.856406460551018)], [(-3.0, 31.712812921102035), (-3.0, 40.95041722813605), (5.0, 45.569219381653056), (13.0, 40.95041722813605), (13.0, 31.712812921102035), (5.0, 27.09401076758503), (-3.0, 31.712812921102035)], [(13.0, 31.712812921102035), (13.0, 40.95041722813605), (21.0, 45.569219381653056), (29.0, 40.95041722813605), (29.0, 31.712812921102035), (21.0, 27.09401076758503), (13.0, 31.712812921102035)]]