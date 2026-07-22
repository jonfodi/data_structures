import time
import random
from bisect import bisect_left

# DATA 
# - EVENT (like a login session, click, etc)
# - TIMESTAMP (time the event happened at)

# QUESTION 1 : FIND THE NUMBER OF OCCURENCES FOR AN EVENT IN THE LAST 5 MINUTES
# we need a link between multiple timestamps and their events, dict makes the most sense 
# we then need a count of all the timestamps between now - 5 minutes 
# the list is naturally sorted by first to last, meaning we can either sort into descending or keep 
# more importantly this is a monotonic problem. all of the data is false until a flip where they all become true 
# which means if we find the cutoff point we can bisect 
# and because the data is in ascending order, we want to bisect (remove) everything on the left 



NOW = 1000               # "now" is 1000 seconds
WINDOW = 5 * 60          # 300 seconds
CUTOFF = NOW - WINDOW    # 700  -> anything at or after 700 is in the window

events = {
    #                <-- older ------------------- newer -->
    "login":    [100, 300, 500, 650, 720, 800, 950],
    "click":    [50, 400, 750, 900],
    "purchase": [710, 720, 730],
    "logout":   [10, 200, 500],
}


def record(event_type, timestamp):
    if event_type in events:
        events[event_type].append(timestamp)
    else:
        events[event_type] = [timestamp]


def count(event_type) -> int:
    timestamps = events.get(event_type, [])
    print(bisect_left(timestamps, CUTOFF))
    # return len(timestamps) - bisect_left(timestamps, CUTOFF)


def total_count() -> int:
    return sum(count(event_type) for event_type in events)


print(count("login"))     # 3  -> 720, 800, 950
print(count("purchase"))  # 3  -> all of them
print(count("logout"))    # 0  -> none of them
print(total_count())      # 8