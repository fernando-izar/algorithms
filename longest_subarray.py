class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        best = 0

        for right, val in enumerate(nums):
            if val == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            best = max(best, right - left)
        return best


solution = Solution()

list_test = [1, 1, 0, 0, 1, 1, 1, 0, 1]

solution.longestSubarray(list_test)
