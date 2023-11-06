#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        land = []
        for i in range(n):
            for j in range(n):
                if not grid[i][j]:
                    continue
                land.append((i, j, 0))
        
        if len(land) == 0 or len(land) == n * n:
            return -1

        q = deque(land)
        while q:
            row, col, dist = q.popleft()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r = row + dr
                c = col + dc
                if not 0 <= r < n or not 0 <= c < n or grid[r][c] != 0:
                    continue
                grid[r][c] = dist + 1
                q.append((r, c, dist + 1))
        
        maxDist = 0
        for i in range(n):
            maxDist = max(maxDist, max(grid[i]))
        return maxDist
        
# @lc code=end

