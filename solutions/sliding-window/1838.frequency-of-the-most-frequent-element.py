#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        runningSum = 0
        maxLength = 0
        while r < len(nums):
            runningSum += nums[r]

            while nums[r] * (r - l + 1) - runningSum > k:
                runningSum -= nums[l]
                l += 1

            maxLength = max(maxLength, r - l + 1)
            r += 1
        return maxLength
        
# @lc code=end

