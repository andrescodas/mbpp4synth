def search(arr,n) :
    """
    Write a python function to find the element that appears only once in a sorted array.
    """
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
    return (XOR)
