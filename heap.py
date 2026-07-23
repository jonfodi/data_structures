from bisect import bisect_left
from heapq import heappush, heappop

NOW = 1000
WINDOW = 5 * 60          # 300
CUTOFF = NOW - WINDOW    # 700

views = {
    #                <-- older ------------------ newer -->
    "home":     [100, 300, 720, 750, 800, 900, 950],   # 5 in window
    "pricing":  [50, 400, 750, 900],                   # 2 in window
    "docs":     [710, 720, 730],                       # 3 in window
    "about":    [10, 200, 500],                        # 0 in window
    "blog":     [705, 800, 850, 990],                  # 4 in window
}
total_count = [5, 60, 720, 800, 900, 945, 955]

def record(page_id, timestamp):
    if page_id in views:
        views[page_id].append(timestamp)
    else:
        views[page_id] = [timestamp]
    
    total_count.append(timestamp)

# this is for when your data is monotomic. consecutive values (i0 -> i1 -> i2) are false until they're all true. 
# the flip point is the cutoff
# since the indicies of the timestamp list implicitly carry the time relation, all timestamps will be within 5 minutes once the first index > 5 minutes is hit
def count(page_id) -> int:
    timestamps = views.get(page_id, [])
    return len(timestamps) - bisect_left(timestamps, CUTOFF)


def top_k(k) -> list:
    heap = []
    for page_id in views:
        heappush(heap, (count(page_id), page_id))
        print(heap)
        if len(heap) > k:
            heappop(heap)
            print(heap)
    return sorted(heap, reverse=True)

def total_number_events(CUTOFF):
    return len(total_count) - bisect_left(total_count, CUTOFF)

res = top_k(3)
print("result = ")
print(res)
print(total_number_events(CUTOFF))
