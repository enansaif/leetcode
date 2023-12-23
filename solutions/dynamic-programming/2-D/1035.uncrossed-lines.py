#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# Tabulation solution
# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 - 1, - 1, - 1):
            for j in range(n2 - 1, - 1, - 1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]
        
# @lc code=end

# Memoization solution
def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
    cache = {}
    def dfs(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i == len(nums1) or j == len(nums2):
            return 0
        if nums1[i] == nums2[j]:
            return dfs(i + 1, j + 1) + 1
        left = dfs(i + 1, j)
        right = dfs(i, j + 1)
        cache[(i, j)] = max(left, right)
        return cache[(i, j)]
    return dfs(0, 0)