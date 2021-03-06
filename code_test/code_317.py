from itertools import groupby
def modified_encode(alist):
        """
        Write a function to reflect the modified run-length encoding from a list.
        """
        def ctr_ele(el):
            if len(el)>1: return [len(el), el[0]]
            else: return el[0]
        return [ctr_ele(list(group)) for key, group in groupby(alist)]
