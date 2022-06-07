import bisect
def left_insertion(a, x):
    """
    Write a function to locate the left insertion point for a specified value in sorted order.
    """
    i = bisect.bisect_left(a, x)
    return i
