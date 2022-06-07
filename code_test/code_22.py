def find_first_duplicate(nums):
    """
    Write a function to find the first duplicate element in a given array of integers.
    """
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate
