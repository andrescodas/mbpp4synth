def sum_even_odd(list1):
    """
    Write a function to find the sum of first even and odd number of a given list.
    """
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even+first_odd)
