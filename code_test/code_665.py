def move_last(num_list):
    """
    Write a python function to shift first element to the end of given list.
    """
    a = [num_list[0] for i in range(num_list.count(num_list[0]))]
    x = [ i for i in num_list if i != num_list[0]]
    x.extend(a)
    return (x)
