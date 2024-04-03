#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (not 0 <= r < ROWS or 
                not 0 <= c < COLS or 
                board[r][c]!= word[i] or 
                (r, c) in visited):
                return False
            visited.add((r, c))
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                if dfs(r + dr, c + dc, i + 1):
                    return True
            visited.remove((r, c))
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
# @lc code=end

