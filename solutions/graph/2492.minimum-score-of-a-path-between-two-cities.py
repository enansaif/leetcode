#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#

# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {k:[] for k in range(1, n + 1)}

        for src, dst, dist in roads:
            graph[src].append((dst, dist))
            graph[dst].append((src, dist))
        
        visited = set()
        min_val = [float('inf')]
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nbr, dist in graph[node]:
                min_val[0] = min(min_val[0], dist)
                dfs(nbr)
        dfs(1)
        return min_val[0]
        
# @lc code=end

