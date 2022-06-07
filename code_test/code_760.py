def unique_Element(arr,n):
    """
    Write a python function to check whether an array contains only one distinct element or not.
    """
    s = set(arr)
    if (len(s) == 1):
        return ('YES')
    else:
        return ('NO')
