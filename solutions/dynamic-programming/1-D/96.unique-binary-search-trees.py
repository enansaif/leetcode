#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# Tabulation Solution
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            total = 0
            for j in range(1, i + 1):
                total += dp[j - 1] * dp[i - j]
            dp[i] = total
        return dp[n]

# @lc code=end

# Memoization Solution
class Solution:
    cache = {}
    def numTrees(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]
        if n < 2:
            return 1
        total = 0
        for i in range(1, n + 1):
            total += self.numTrees(i - 1) * self.numTrees(n - i)
        Solution.cache[n] = total
        return total
