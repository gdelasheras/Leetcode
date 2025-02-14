"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, 
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). 

Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

T: O(n) where n is the number of calls to ping.
S: O(n) where n is the number of elements store in the queue.
"""

from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = deque([])

    def ping(self, t: int) -> int:
        def clean():
            current_t = self.queue[0]
            while current_t < t - 3000:
                self.queue.popleft()
                current_t = self.queue[0]

        self.queue.append(t)
        clean()
        return len(self.queue)


def test_RecentCounter():
    r = RecentCounter()
    assert r.ping(1) == 1
    assert r.ping(100) == 2
    assert r.ping(3001) == 3
    assert r.ping(3002) == 3
