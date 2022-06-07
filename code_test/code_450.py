def extract_string(str, l):
    """
    Write a function to extract specified size of strings from a give list of string values.
    """
    result = [e for e in str if len(e) == l] 
    return result
