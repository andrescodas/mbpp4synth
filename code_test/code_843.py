import heapq
def nth_super_ugly_number(n, primes):
    """
    Write a function to find the nth super ugly number from a given prime list of size k using heap queue algorithm.
    """
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
            yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]
