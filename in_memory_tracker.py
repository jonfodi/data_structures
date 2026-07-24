from bisect import bisect_left, insort
from heapq import heappush, heappop
from collections import defaultdict

from view_tracker import ViewTracker


class InMemoryViewTracker(ViewTracker):
    def __init__(self, window=300):
        self.window = window
        self.page_views = defaultdict(list) # { page_id: [timestamps] }
        self.total_views = []
        self.heap = []

    def record(self, page_id, ts):
        self.page_views[page_id].append(ts)
        insort(self.total_views, ts)
        
    def count_in_window(self, page_id, now):
        ts = self.page_views.get(page_id, [])
        return len(ts) - bisect_left(ts, now - self.window)

    def top_k(self, k, now):
        # this implementation is dependant on dictionary keys. as that grows, this becomes less space/time eff. 
        # res = []
        # for page_id in self.page_views:
        #     number_of_visits = self.count_in_window(page_id, now)
        #     res.append((number_of_visits, page_id))
        #     res = sorted(res, reverse=True)
        #     if len(res) > k:
        #         res.pop()
        # return res
        heap = []
        for page_id in self.page_views:
            heappush(heap, (count_in_window(page_id, now), page_id))
            if len(heap) > k:
                heappop(heap)
            return sorted(heap, reverse=True)

    def least_k(self, k, now):
        res = []
        for page_id in self.page_views:
            res.append((self.count_in_window(page_id, now), page_id))
            res = sorted(res)
            if len(res) > k:
                res.pop()
        return res
        
    def total_in_window(self, now):
        return len(self.total_page_views) - bisect_left(self.total_page_views, now - self.window)

    def total_views_of_page(self, page_id) -> int:
        return len(self.page_views[page_id])
    
    def all_views(self) -> int:
        return len(total_views)
    
    def least_number_views(self) -> tuple:
        # (view_count, page_id)
        res = []
        for page_id in self.page_views:
            tup = (self.total_views_of_page(page_id), page_id)
            res.append(tup)
        return sorted(res)[0]
