from view_tracker import ViewTracker

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
print(tracker.least_number_views)