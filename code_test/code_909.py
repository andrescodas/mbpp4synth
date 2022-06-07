def previous_palindrome(num):
    """
    Write a function to find the previous palindrome of a specified number.
    """
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
