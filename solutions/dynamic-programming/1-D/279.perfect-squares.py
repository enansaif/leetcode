#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# Top down
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dfs(num):
            if num in cache:
                return cache[num]
            if num < 4:
                return num
            min_sq = float('inf')
            for i in range(2, int(sqrt(n)) + 1):
                if num - i**2 >= 0:
                    min_sq = min(min_sq, dfs(num - i**2) + 1)
                else:
                    break
            cache[num] = min_sq
            return min_sq
        return dfs(n)

# Bottom up
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                
        return dp[n]
        
# @lc code=end

