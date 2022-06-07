def sector_area(r,a):
    """
    Write a function to find area of a sector.
    """
    pi=22/7
    if a >= 360:
        return None
    sectorarea = (pi*r**2) * (a/360)
    return sectorarea
