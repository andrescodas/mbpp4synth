def sum_of_digits(nums):
    """
    Write a function to compute the sum of digits of each number of a given list.
    """
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())
