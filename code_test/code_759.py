def is_decimal(num):
    """
    Write a function to check a decimal with a precision of 2.
    """
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)
