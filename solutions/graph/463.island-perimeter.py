#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or not grid[r][c]:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            count = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                count += dfs(r + dr, c + dc)
            return count
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i, j)
        
# @lc code=end

