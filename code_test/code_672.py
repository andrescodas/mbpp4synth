def max_of_three(num1,num2,num3): 
    """
    Write a function to find maximum of three numbers.
    """
    if (num1 >= num2) and (num1 >= num3):
       lnum = num1
    elif (num2 >= num1) and (num2 >= num3):
       lnum = num2
    else:
       lnum = num3
    return lnum
