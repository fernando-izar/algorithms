from collections import deque


class Solution:
    def maxArea(self, height: list[int]) -> int:
        d = deque(height)
        max_vol = 0
        while d:
            temp_vol = min(d[0], d[-1]) * (len(d) - 1)
            max_vol = temp_vol if temp_vol > max_vol else max_vol
            if d[0] < d[-1]:
                d.popleft()
            else:
                d.pop()
        return max_vol


l = [1, 8, 6, 2, 5, 4, 8, 3, 7]

s = Solution()
resp = s.maxArea(l)

print(resp)
