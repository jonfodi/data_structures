from view_tracker import ViewTracker


class RedisViewTracker(ViewTracker):
    def __init__(self, redis_client, window=300):
        self.redis = redis_client
        self.window = window

    def record(self, page_id, ts):
        self.redis.zadd(f"views:{page_id}", {ts: ts})
        self.redis.zadd("views:__total__", {f"{page_id}:{ts}": ts})

    def count_in_window(self, page_id, now):
        return self.redis.zcount(f"views:{page_id}", now - self.window, now)

    def top_k(self, k, now):
        keys = self.redis.keys("views:*")
        counts = [(self.count_in_window(key.split(":")[1], now), key.split(":")[1]) for key in keys]
        return sorted(counts, reverse=True)[:k]

    def total_in_window(self, now):
        return self.redis.zcount("views:__total__", now - self.window, now)
    
    def total_views_of_page(self, page_id) -> int: 
        pass

    def all_views(self) -> int: 
        pass

    def least_number_views(self, page_id) -> tuple: 
        pass