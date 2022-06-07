def count_digits(num1,num2):
    """
    Write a function to add two numbers and print number of digits of sum.
    """
    number=num1+num2
    count = 0
    while(number > 0):
        number = number // 10
        count = count + 1
    return count
