from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        idx_R = deque()
        idx_D = deque()

        for i, value in enumerate(senate):
            if value == "D":
                idx_D.append(i)
            else:
                idx_R.append(i)

        l = len(senate)

        while len(idx_D) and len(idx_R):
            if idx_D[0] < idx_R[0]:
                idx_D.append(idx_D[0] + l)
            else:
                idx_R.append(idx_R[0] + l)
            idx_D.popleft()
            idx_R.popleft()

        if idx_D:
            return "Dire"

        return "Radiant"


senate = "RDD"
solution = Solution()
print(solution.predictPartyVictory(senate))
