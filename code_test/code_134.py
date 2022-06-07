"""
Write a python function to check whether the last element of given array is even or odd after performing an operation p times.
"""
def check_last (arr,n,p): 
    _sum = 0
    for i in range(n): 
        _sum = _sum + arr[i] 
    if p == 1: 
        if _sum % 2 == 0: 
            return "ODD"
        else: 
            return "EVEN"
    return "EVEN"
      
