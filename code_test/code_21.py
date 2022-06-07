def multiples_of_num(m,n): 
    """
    Write a function to find m number of multiples of n.
    """
    multiples_of_num= list(range(n,(m+1)*n, n)) 
    return list(multiples_of_num)
