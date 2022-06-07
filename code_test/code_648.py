from itertools import zip_longest, chain, tee
def exchange_elements(lst):
    """
    Write a function to exchange the position of every n-th value with (n+1)th value and (n+1)th value with n-th value in a given list.
    """
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
