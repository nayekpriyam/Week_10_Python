def min_platforms(arrivals, departures):
    arrivals_sorted = sorted(arrivals)
    departures_sorted = sorted(departures)
    i = j = 0
    needed = 0
    max_needed = 0
    n = len(arrivals)
    while i < n and j < n:
        if arrivals_sorted[i] <= departures_sorted[j]:
            needed += 1
            max_needed = max(max_needed, needed)
            i += 1
        else:
            needed -= 1
            j += 1
    return max_needed
