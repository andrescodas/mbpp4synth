def prime_num(num):
  """
  Write a function to check if the given integer is a prime number.
  """
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
