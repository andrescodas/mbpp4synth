from collections import Counter
from itertools import chain
def freq_element(nums):
  """
  Write a function to find frequency of the elements in a given list of lists using collections module.
  """
  result = Counter(chain.from_iterable(nums))
  return result
