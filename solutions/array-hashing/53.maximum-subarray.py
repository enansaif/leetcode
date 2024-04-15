#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        glob_max = max(nums)
        curr_max = 0
        for n in nums:
            curr_max += n
            glob_max = max(curr_max, glob_max)
            curr_max = max(0, curr_max)
        return glob_max
        
# @lc code=end

