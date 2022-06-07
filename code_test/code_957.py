import math
def get_First_Set_Bit_Pos(n):
     """
     Write a python function to get the position of rightmost set bit.
     """
     return math.log2(n&-n)+1
