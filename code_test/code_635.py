import heapq as hq
def heap_sort(iterable):
    """
    Write a function to push all values into a heap and then pop off the smallest values one at a time.
    """
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]
