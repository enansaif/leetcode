#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        min_cost = sum([1 for c in s if c == '0'])
        
        cost = min_cost
        for i in range(len(s)):
            cost = cost - 1 if s[i] == '0' else cost + 1
            min_cost = min(min_cost, cost)
        
        return min_cost
        
# @lc code=end

