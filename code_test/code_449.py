def check_Triangle(x1,y1,x2,y2,x3,y3): 
    """
    Write a python function to check whether the triangle is valid or not if 3 points are given.
    """
    a = (x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))   
    if a == 0: 
        return ('No') 
    else: 
        return ('Yes') 
