def digit_distance_nums(n1, n2):
         """
         Write a python function to find the digit distance between two integers.
         """
         return sum(map(int,str(abs(n1-n2))))
