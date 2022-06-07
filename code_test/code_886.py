def sum_num(numbers):
    """
    Write a function to add all the numbers in a list and divide it with the length of the list.
    """
    total = 0
    for x in numbers:
        total += x
    return total/len(numbers) 
