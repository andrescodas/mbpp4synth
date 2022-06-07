from operator import itemgetter
def index_on_inner_list(list_data, index_no):
    """
    Write a function to sort a list of lists by a given index of the inner list.
    """
    result = sorted(list_data, key=itemgetter(index_no))
    return result
