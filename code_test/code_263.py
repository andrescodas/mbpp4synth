def merge_dict(d1,d2):
 """
 Write a function to merge two dictionaries.
 """
 d = d1.copy()
 d.update(d2)
 return d
