def find_platform(arr, dep, n): 
    """
    Write a function to find the minimum number of platforms required for a railway/bus station.
    """
    arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n): 
        if (arr[i] <= dep[j]):           
            plat_needed+= 1
            i+= 1
        elif (arr[i] > dep[j]):           
            plat_needed-= 1
            j+= 1
        if (plat_needed > result):  
            result = plat_needed           
    return result
