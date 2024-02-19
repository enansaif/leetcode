#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if (i, prev) in cache:
                return cache[(i, prev)]
            if i == len(nums):
                return 0
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = dfs(i + 1, i) + 1
            skip = dfs(i + 1, prev)
            cache[(i, prev)] = max(take, skip)
            return cache[(i, prev)]
        
        return dfs(0, -1)
        
# @lc code=end

