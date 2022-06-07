def odd_Days(N): 
    """
    Write a python function to calculate the number of odd days in a given year.
    """
    hund1 = N // 100
    hund4 = N // 400
    leap = N >> 2
    ordd = N - leap 
    if (hund1): 
        ordd += hund1 
        leap -= hund1 
    if (hund4): 
        ordd -= hund4 
        leap += hund4 
    days = ordd + leap * 2
    odd = days % 7
    return odd 
