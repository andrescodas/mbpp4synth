def dig_let(s):
 """
 Write a function to calculate the number of digits and letters in a string.
 """
 d=l=0
 for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
 return (l,d)
