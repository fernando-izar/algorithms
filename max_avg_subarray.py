class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        avg = float("-inf")
        prod = 0
        start = 0

        for i, value in enumerate(nums):
            prod += value
            if i == k - 1:
                avg = prod / k
            if i - start >= k:
                prod -= nums[start]
                start += 1
                if avg < prod / k:
                    avg = prod / k
        return avg

    def findMaxAverage_(self, nums: list[int], k: int) -> float:

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4

solution = Solution()
print(solution.findMaxAverage_(nums, k))
