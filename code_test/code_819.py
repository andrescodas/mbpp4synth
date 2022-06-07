def count_duplic(lists):
    """
    Write a function to count the frequency of consecutive duplicate elements in a given list of numbers.
    """
    element = []
    frequency = []
    if not lists:
        return element
    running_count = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            running_count += 1
        else:
            frequency.append(running_count)
            element.append(lists[i])
            running_count = 1
    frequency.append(running_count)
    element.append(lists[i+1])
    return element,frequency
