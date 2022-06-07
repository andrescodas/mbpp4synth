MAX=1000;
def replace_spaces(string):
  """
  Write a function to replace all spaces in the given string with character * list item * list item * list item * list item '%20'.
  """
  string=string.strip()
  i=len(string)
  space_count=string.count(' ')
  new_length = i + space_count*2
  if new_length > MAX:
    return -1
  index = new_length-1
  string=list(string)
  for f in range(i-2, new_length-2):
    string.append('0')
  for j in range(i-1, 0, -1):
    if string[j] == ' ':
      string[index] = '0'
      string[index-1] = '2'
      string[index-2] = '%'
      index=index-3
    else:
      string[index] = string[j]
      index -= 1
  return ''.join(string)
