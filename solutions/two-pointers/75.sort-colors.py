#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# Optimized solution
# time complexity: O(n) (single pass)
# space complexity: O(n)
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
                
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
