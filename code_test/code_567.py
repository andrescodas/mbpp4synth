def issort_list(list1):
    """
    Write a function to check whether a specified list is sorted or not.
    """
    result = all(list1[i] <= list1[i+1] for i in range(len(list1)-1))
    return result
