def find_Max_Num(arr,n) : 
    """
    Write a python function to find the largest number that can be formed with the given digits.
    """
    arr.sort(reverse = True) 
    num = arr[0] 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
    return num 
