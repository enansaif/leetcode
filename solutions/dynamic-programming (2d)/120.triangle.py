#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# Tabulation Solution
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, - 1, - 1):
            for j in range(len(triangle[i]) - 1, - 1, - 1):
                triangle[i][j] += min(triangle[i + 1][j], 
                                      triangle[i + 1][j + 1])
        return triangle[0][0]
        
# @lc code=end

# Memoization Solution
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == len(triangle):
                return 0
            down = dfs(r + 1, c)
            right = dfs(r + 1, c + 1)
            cache[(r, c)] = min(down, right) + triangle[r][c]
            return cache[(r, c)]
        return dfs(0, 0)

