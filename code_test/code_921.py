def chunk_tuples(test_tup, N):
  """
  Write a function to perform chunking of tuples each of size n.
  """
  res = [test_tup[i : i + N] for i in range(0, len(test_tup), N)]
  return (res) 
