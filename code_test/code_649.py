def sum_Range_list(nums, m, n):                                                                                                                                                                                                
    """
    Write a python function to calculate the sum of the numbers in a list between the indices of a specified range.
    """
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += nums[i]                                                                                                                                                                                                  
    return sum_range   
