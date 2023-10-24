#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# Binary search solution
# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return nums[l]
            m = (l + r) // 2
            if nums[m] != nums[m - 1]:
                if (m - l) % 2 == 0:
                    l = m
                else:
                    r = m - 1
            else:
                if (r - m) % 2 == 0:
                    r = m
                else:
                    l = m + 1
        
# @lc code=end

# O(n) solution with bit-wise multiplication
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result
