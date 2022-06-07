def sum_average(number):
 """
 Write a function to find sum and average of first n natural numbers.
 """
 total = 0
 for value in range(1, number + 1):
    total = total + value
 average = total / number
 return (total,average)
