def sum_difference(n):
    """
    Write a function to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.
    """
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, n+1):
        sumofsquares += num * num
        squareofsum += num
    squareofsum = squareofsum ** 2
    return squareofsum - sumofsquares
