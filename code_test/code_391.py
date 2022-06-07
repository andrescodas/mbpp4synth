def convert_list_dictionary(l1, l2, l3):
     """
     Write a function to convert more than one list to nested dictionary.
     """
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
