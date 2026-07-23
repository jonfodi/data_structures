from in_memory_tracker import InMemoryViewTracker
from redis_tracker import RedisViewTracker


def make_tracker(redis_client=None, window=300):
    if redis_client:
        return RedisViewTracker(redis_client, window)
    return InMemoryViewTracker(window)
