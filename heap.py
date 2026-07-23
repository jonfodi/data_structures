from bisect import bisect_left
from heapq import heappush, heappop
from collections import defaultdict

class ViewTracker:
    def __init__(self, window=300):
        self.window = window
        self.views = defaultdict(list)
        self.total_views = []

    def record(self, page_id, ts):
        self.views[page_id].append(ts)
        self.total_views.append(ts)

    def count_in_window(self, page_id, now):
        ts = self.views.get(page_id, [])
        return len(ts) - bisect_left(ts, now - self.window)

    def top_k(self, k, now):
        heap = []
        for page_id in self.views:
            heappush(heap, (self.count_in_window(page_id, now), page_id))
            if len(heap) > k:
                heappop(heap)
        return sorted(heap, reverse=True)

    def total_in_window(self, now):
        return len(self.total_views) - bisect_left(self.total_views, now - self.window)


views = {
    #                <-- older ------------------ newer -->
    "home":     [100, 300, 720, 750, 800, 900, 950],   # 5 in window
    "pricing":  [50, 400, 750, 900],                   # 2 in window
    "docs":     [710, 720, 730],                       # 3 in window
    "about":    [10, 200, 500],                        # 0 in window
    "blog":     [705, 800, 850, 990],                  # 4 in window
}

tracker = ViewTracker()

for page_id, timestamps in views.items():
    for ts in timestamps:
        tracker.record(page_id, ts)

tracker.total_views.sort()

print(tracker.top_k(3, now=1000))          # [(5, 'home'), (4, 'blog'), (3, 'docs')]
print(tracker.total_in_window(now=1000))   # 14