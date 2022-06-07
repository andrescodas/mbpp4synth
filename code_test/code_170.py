def sum_range_list(list1, m, n):                                                                                                                                                                                                
    """
    Write a function to find sum of the numbers in a list between the indices of a specified range.
    """
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += list1[i]                                                                                                                                                                                                  
    return sum_range   
