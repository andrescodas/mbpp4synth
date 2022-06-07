from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    """
    Write a function to choose specified number of colours from three different colours and generate all the combinations with repetitions.
    """
    return list(combinations_with_replacement(l,n))
