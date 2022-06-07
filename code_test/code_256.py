def count_Primes_nums(n):
    """
    Write a python function to count the number of prime numbers less than a given non-negative number.
    """
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
