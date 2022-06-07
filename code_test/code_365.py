def count_Digit(n):
    """
    Write a python function to count the number of digits of a given number.
    """
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
