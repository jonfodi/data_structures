from view_tracker import ViewTracker
from factory import make_tracker




if __name__ == "__main__":

    views = {
        #                <-- older ------------------ newer -->
        "home":     [100, 300, 720, 750, 800, 900, 950],   # 5 in window
        "pricing":  [50, 400, 750, 900],                   # 2 in window
        "docs":     [710, 720, 730],                       # 3 in window
        "about":    [10, 200, 500],                        # 0 in window
        "blog":     [705, 800, 850, 990],                  # 4 in window
    }
    now = 1000

    tracker = make_tracker(redis_client=None, window=300)

    for page_id, timestamps in views.items():
        for ts in timestamps:
            tracker.record(page_id, ts)

    print(tracker.top_k(3, now=now))
    print(tracker.total_in_window(now=now))

    (views, page) = tracker.least_number_views()
    print(f"{page} has the least number of views with: {views}")

    least_views = tracker.least_k(3, 1000)
