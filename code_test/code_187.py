def longest_common_subsequence(X, Y, m, n): 
    """
    Write a function to find the longest common subsequence for the given two sequences.
    """
    if m == 0 or n == 0: 
       return 0 
    elif X[m-1] == Y[n-1]: 
       return 1 + longest_common_subsequence(X, Y, m-1, n-1) 
    else: 
       return max(longest_common_subsequence(X, Y, m, n-1), longest_common_subsequence(X, Y, m-1, n))
