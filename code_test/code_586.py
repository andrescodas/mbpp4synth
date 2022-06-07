def split_Arr(a,n,k):  
   """
   Write a python function to split the array and add the first part to the end.
   """
   b = a[:k] 
   return (a[k::]+b[::]) 
