def reverse_Array_Upto_K(input, k): 
  """
  Write a python function to reverse an array upto a given position.
  """
  return (input[k-1::-1] + input[k:]) 
