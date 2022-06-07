def maximum_Sum(list1): 
    """
    Write a python function to find the maximum sum of elements of list in a list of lists.
    """
    maxi = -100000
    for x in list1: 
        sum = 0 
        for y in x: 
            sum+= y      
        maxi = max(sum,maxi)     
    return maxi 
