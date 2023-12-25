#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS:
                return 0
            if (r, c) in visited or grid[r][c] == 1:
                return 1
            visited.add((r, c))
            isClosed = 1
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                isClosed = min(isClosed, dfs(r + dr, c + dc))
            return isClosed

        count = 0
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    continue
                if (i, j) not in visited:
                    count += dfs(i, j)
        return count
        
# @lc code=end

