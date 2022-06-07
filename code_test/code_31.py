def func(nums, k):
    """
    Write a function to find the top k integers that occur most frequently from given lists of sorted and distinct integers using heap queue algorithm.
    """
    import collections
    d = collections.defaultdict(int)
    for row in nums:
        for i in row:
            d[i] += 1
    temp = []
    import heapq
    for key, v in d.items():
        if len(temp) < k:
            temp.append((v, key))
            if len(temp) == k:
                heapq.heapify(temp)
        else:
            if v > temp[0][0]:
                heapq.heappop(temp)
                heapq.heappush(temp, (v, key))
    result = []
    while temp:
        v, key = heapq.heappop(temp)
        result.append(key)
    return result
