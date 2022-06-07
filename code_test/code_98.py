def multiply_num(numbers):  
    """
    Write a function to multiply all the numbers in a list and divide with the length of the list.
    """
    total = 1
    for x in numbers:
        total *= x  
    return total/len(numbers) 
