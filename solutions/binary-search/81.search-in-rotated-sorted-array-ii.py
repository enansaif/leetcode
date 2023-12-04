#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[m] < nums[l]:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[l]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1
        return False
        
        
# @lc code=end

