import sys
def next_smallest_palindrome(num):
    """
    Write a function to find the next smallest palindrome of a specified number.
    """
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
