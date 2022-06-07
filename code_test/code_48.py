def odd_bit_set_number(n):
    """
    Write a python function to set all odd bits of a given number.
    """
    count = 0;res = 0;temp = n
    while temp > 0:
        if count % 2 == 0:
            res |= (1 << count)
        count += 1
        temp >>= 1
    return (n | res)
