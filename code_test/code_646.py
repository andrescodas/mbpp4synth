def No_of_cubes(N,K):
    """
    Write a python function to count number of cubes of size k in a cube of size n.
    """
    No = 0
    No = (N - K + 1)
    No = pow(No, 3)
    return No
