def remove_kth_element(list1, L):
    """
    Write a python function to remove the k'th element from a given list.
    """
    return  list1[:L-1] + list1[L:]
