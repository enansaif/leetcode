#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        def dfs(r, c, is_sub_island):
            if not 0 <= r < ROWS or not 0 <= c < COLS or not grid2[r][c]:
                return is_sub_island
            if not grid1[r][c]:
                is_sub_island = False
            grid2[r][c] = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                is_sub_island = dfs(r + dr, c + dc, is_sub_island)
            return is_sub_island
        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if not grid2[i][j]:
                    continue
                if dfs(i, j, True):
                    count += 1
        return count
        
# @lc code=end

