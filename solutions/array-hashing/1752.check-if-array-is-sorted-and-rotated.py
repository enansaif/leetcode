#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        pivot = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = i
                break
        
        for i in range(1, len(nums)):
            if nums[(pivot + i - 1)%len(nums)] > nums[(pivot + i)%len(nums)]:
                return False
        return True
# @lc code=end

