def move_zero(num_list):
    """
    Write a python function to move all zeroes to the end of the given list.
    """
    a = [0 for i in range(num_list.count(0))]
    x = [ i for i in num_list if i != 0]
    x.extend(a)
    return (x)
