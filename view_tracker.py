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

    def count(self, page_id):
        return len(self.views[page_id])

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
    
    def least_number_views(self):
        # mid as f, arguably worse than that 
        # heap = []
        # for page_id in self.views:
        #     heappush(heap, (self.count(page_id), page_id))
        # return heap[0]
        return min((self.count(p), p) for p in self.views)

