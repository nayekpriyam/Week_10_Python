from collections import defaultdict

def sherlock_and_anagrams(s):
    n = len(s)
    freq = defaultdict(int)
    for i in range(n):
        counts = [0]*26
        for j in range(i, n):
            counts[ord(s[j]) - ord('a')] += 1
            key = tuple(counts)
            freq[key] += 1
    total_pairs = 0
    for count in freq.values():
        total_pairs += count * (count - 1) // 2
    return total_pairs
