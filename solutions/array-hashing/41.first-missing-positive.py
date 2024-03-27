#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        
        for n in nums:
            if 1 <= abs(n) <= len(nums):
                nums[abs(n) - 1] = -1 * abs(nums[abs(n) - 1])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
        
# @lc code=end

