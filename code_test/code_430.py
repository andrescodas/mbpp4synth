def parabola_directrix(a, b, c): 
  """
  Write a function to find the directrix of a parabola.
  """
  directrix=((int)(c - ((b * b) + 1) * 4 * a ))
  return directrix
