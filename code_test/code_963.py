def discriminant_value(x,y,z):
    """
    Write a function to calculate the discriminant value.
    """
    discriminant = (y**2) - (4*x*z)
    if discriminant > 0:
        return ("Two solutions",discriminant)
    elif discriminant == 0:
        return ("one solution",discriminant)
    elif discriminant < 0:
        return ("no real solution",discriminant)
