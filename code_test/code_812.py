import re
def road_rd(street):
  """
  Write a function to abbreviate 'road' as 'rd.' in a given string.
  """
  return (re.sub('Road$', 'Rd.', street))
