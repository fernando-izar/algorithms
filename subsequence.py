class Solution:
    def isSubsequence_k(self, s: list, t: str) -> bool:
        if not s:
            return True

        for i_t in range(len(t)):
            for i, s_item in enumerate(s):
                if not isinstance(s_item, list):
                    s[i] = [s_item, len(s_item), 0]
                if s[i][1] > s[i][2]:
                    if s[i][0][s[i][2]] == t[i_t]:
                        s[i][2] += 1
                    if s[i][1] - s[i][2] > len(t) - i_t:
                        return False
        return True


s = ["ab", "ef", "xy"]
# s = ["gh"]

t = "aeibfc"

solution = Solution()
print(solution.isSubsequence_k(s, t))
