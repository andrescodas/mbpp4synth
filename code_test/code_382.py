def find_rotation_count(A):
    """
    Write a function to find the number of rotations in a circularly sorted array.
    """
    (left, right) = (0, len(A) - 1)
    while left <= right:
        if A[left] <= A[right]:
            return left
        mid = (left + right) // 2
        next = (mid + 1) % len(A)
        prev = (mid - 1 + len(A)) % len(A)
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            return mid
        elif A[mid] <= A[right]:
            right = mid - 1
        elif A[mid] >= A[left]:
            left = mid + 1
    return -1
