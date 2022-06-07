from itertools import groupby 
def extract_elements(numbers, n):
    """
    Write a function to extract specified number of elements from a given list, which follow each other continuously.
    """
    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 
    return result
