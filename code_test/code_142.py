def count_samepair(list1,list2,list3):
    """
    Write a function to count the same pair in three given lists.
    """
    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))
    return result
