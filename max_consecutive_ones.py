from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        best = 0

        for r, v in enumerate(nums):
            if v == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            best = max(best, r - l + 1)

        return best


nums = [1, 1, 1]
k = 2
s = Solution()
print(s.longestOnes(nums, 2))
