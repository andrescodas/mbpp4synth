def find_Sum(arr,n): 
    """
    Write a python function to find the sum of non-repeated elements in a given array.
    """
    arr.sort() 
    sum = arr[0] 
    for i in range(0,n-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
