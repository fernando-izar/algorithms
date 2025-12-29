from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        cutoff = t - 3000
        while self.q and self.q[0] < cutoff:
            self.q.popleft()
        print(len(self.q))
        return len(self.q)


recent_counter = RecentCounter()

recent_counter.ping(0)
recent_counter.ping(1)
recent_counter.ping(100)
recent_counter.ping(3001)
recent_counter.ping(3002)
recent_counter.ping(6000)
recent_counter.ping(6010)
