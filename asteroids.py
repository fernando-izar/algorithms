class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                if abs(a) > stack[-1]:
                    stack.pop()
                    continue
                if abs(a) == stack[-1]:
                    stack.pop()
                alive = False
            if alive:
                stack.append(a)
        return stack


l = [-2, 2, -1, -2]
s = Solution()
response = s.asteroidCollision(l)
print(response)
