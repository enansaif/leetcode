#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        q = deque([(0, 0, 1)])
        while q:
            row, col, pth = q.popleft()
            if row == n - 1 and col == n - 1:
                return pth
            for dr, dc in dirs:
                r = row + dr
                c = col + dc
                if not 0 <= r < n or not 0 <= c < n or grid[r][c]:
                    continue
                q.append((r, c, pth + 1))
                grid[r][c] = 1
        return -1
        
# @lc code=end

