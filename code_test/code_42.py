def find_Sum(arr,n): 
    """
    Write a python function to find the sum of repeated elements in a given array.
    """
    return sum([x for x in arr if arr.count(x) > 1])
