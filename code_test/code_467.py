def decimal_to_Octal(deciNum):
    """
    Write a python function to convert decimal number to octal number.
    """
    octalNum = 0
    countval = 1;
    dNo = deciNum;
    while (deciNum!= 0):
        remainder= deciNum % 8;
        octalNum+= remainder*countval;
        countval= countval*10;
        deciNum //= 8; 
    return (octalNum)
