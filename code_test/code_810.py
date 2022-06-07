from collections import Counter
def count_variable(a,b,c,d):
  """
  Write a function to iterate over elements repeating each as many times as its count.
  """
  c = Counter(p=a, q=b, r=c, s=d)
  return list(c.elements())
