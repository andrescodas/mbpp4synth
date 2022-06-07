def max_val(listval):
     """
     Write a function to find the maximum value in a given heterogeneous list.
     """
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)
