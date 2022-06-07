def power_base_sum(base, power):
    """
    Write a function to calculate the sum of all digits of the base to the specified power.
    """
    return sum([int(i) for i in str(pow(base, power))])
