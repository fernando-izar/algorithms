from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = dict()
        provinces = 0

        for i, cities in enumerate(isConnected):
            if not visited.get(i):
                visited[i] = True
                provinces += 1

            def dfs(connections: list):
                for j, value in enumerate(connections):
                    if i == j:
                        continue
                    elif value == 0:
                        continue
                    else:
                        if not visited.get(j):
                            visited[j] = True
                            dfs(isConnected[j])

            dfs(cities)

        return provinces


s = Solution()
list_test = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
response = s.findCircleNum(list_test)

print(response)
