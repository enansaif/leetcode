#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, count = nums[0], 1
        l = 1
        for i in range(1, len(nums)):
            if prev != nums[i]:
                prev = nums[i]
                count = 1
                nums[l] = nums[i]
                l += 1
            else:
                if count < 2:
                    count += 1
                    nums[l] = nums[i]
                    l += 1
        return l
        
# @lc code=end

