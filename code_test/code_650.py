def are_Equal(arr1,arr2,n,m):
    """
    Write a python function to check whether the given two arrays are equal or not.
    """
    if (n != m):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0,n - 1):
        if (arr1[i] != arr2[i]):
            return False
    return True
