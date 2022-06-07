def sum_div(number):
    """
    Write a function to return the sum of all divisors of a number.
    """
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
