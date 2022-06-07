def filter_data(students,h,w):
    """
    Write a function to filter the height and width of students which are stored in a dictionary.
    """
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    
