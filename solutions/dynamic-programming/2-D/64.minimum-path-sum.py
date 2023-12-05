#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# Memoization solution
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if not 0 <= r < ROWS or not 0 <= c < COLS:
                return float('inf')
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            cache[(r, c)] = min(dfs(r + 1, c), dfs(r, c + 1)) + grid[r][c]
            return cache[(r, c)]
        cache = {}
        ROWS, COLS = len(grid), len(grid[0])
        return dfs(0, 0)
        
# @lc code=end

# Tabulation solution
def minPathSum(self, grid: List[List[int]]) -> int:
    for i in range(len(grid) - 1, - 1, - 1):
        for j in range(len(grid[0]) - 1, - 1, - 1):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                continue
            down = grid[i + 1][j] if i + 1 < len(grid) else float('inf')
            right = grid[i][j + 1] if j + 1 < len(grid[0]) else float('inf')
            grid[i][j] += min(down, right)
    return grid[0][0]