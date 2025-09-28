from collections import Counter
import heapq

def top_k_frequent(nums, k):
    return [val for val, _ in Counter(nums).most_common(k)]
