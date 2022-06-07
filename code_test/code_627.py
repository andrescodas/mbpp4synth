def find_First_Missing(array,start,end): 
    """
    Write a python function to find the smallest missing number from the given array.
    """
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
