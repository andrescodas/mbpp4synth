def Check_Solution(a,b,c) : 
    """
    Write a python function to find number of solutions in quadratic equation.
    """
    if ((b*b) - (4*a*c)) > 0 : 
        return ("2 solutions") 
    elif ((b*b) - (4*a*c)) == 0 : 
        return ("1 solution") 
    else : 
        return ("No solutions") 
