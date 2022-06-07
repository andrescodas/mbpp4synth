def find_Points(l1,r1,l2,r2): 
    """
    Write a python function to choose points from two ranges such that no point lies in both the ranges.
    """
    x = min(l1,l2) if (l1 != l2) else -1
    y = max(r1,r2) if (r1 != r2) else -1
    return (x,y)
