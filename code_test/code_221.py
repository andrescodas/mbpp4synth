def first_even(nums):
    """
    Write a python function to find the first even number in a given list of numbers.
    """
    first_even = next((el for el in nums if el%2==0),-1)
    return first_even
