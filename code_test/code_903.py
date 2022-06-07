def count_Unset_Bits(n) :  
    """
    Write a python function to count the total unset bits from 1 to n.
    """
    cnt = 0;  
    for i in range(1,n + 1) : 
        temp = i;  
        while (temp) :  
            if (temp % 2 == 0) : 
                cnt += 1;  
            temp = temp // 2;  
    return cnt;  
