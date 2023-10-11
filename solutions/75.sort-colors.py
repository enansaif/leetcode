#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
# @lc code=end

# Unoptimized solution
# time complexity: O(N) (two pass)
# space complexity: O(1)
def sortColors(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                
        right = len(nums) - 1
        for i in range(len(nums) - 1, - 1, - 1):
            if nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
