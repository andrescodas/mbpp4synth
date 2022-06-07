def get_Number(n, k): 
    """
    Write a python function to find the kth element in an array containing odd elements first and then even elements.
    """
    arr = [0] * n; 
    i = 0; 
    odd = 1; 
    while (odd <= n):   
        arr[i] = odd; 
        i += 1; 
        odd += 2;
    even = 2; 
    while (even <= n): 
        arr[i] = even; 
        i += 1;
        even += 2; 
    return arr[k - 1]; 
