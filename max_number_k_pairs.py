from typing import List
from collections import Counter


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)

        res = 0
        # repeated = set()

        for x in list(counter.keys()):
            y = k - x
            # if (k - x) in counter and x not in repeated:
            if y in counter:
                if y == x:
                    res += counter[x] // 2
                    del counter[x]
                else:
                    res += min(counter[x], counter[y])
                    # repeated.add(k - x)
                    del counter[x]
                    del counter[y]
        return res

    #     if len(nums) <= 1:
    #         return 0
    #     nums.sort()
    #     i = 0
    #     j = len(nums) - 1
    #     res = 0
    #     while i < j:
    #         if nums[i] + nums[j] == k:
    #             nums.pop(i)
    #             j -= 1
    #             nums.pop(j)
    #             j -= 1
    #             res += 1
    #         elif nums[i] + nums[j] < k:
    #             i += 1
    #         else:
    #             j -= 1

    #     return res


s = Solution()
print(s.maxOperations([1, 2, 3, 4], 5))
