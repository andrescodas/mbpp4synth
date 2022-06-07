def multiply_int(x, y):
    """
    Write a function to multiply two integers without using the * operator in python.
    """
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
