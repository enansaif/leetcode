#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = 0, 0
        curMax, curMin = 0, 0
        for r in range(len(nums)):
            curMax += nums[r]
            curMin += nums[r]
            if curMax < 0:
                curMax = 0
            if curMin > 0:
                curMin = 0
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        ans = max(maxSum, sum(nums) - minSum)
        return ans if ans > 0 else max(nums)
        
# @lc code=end

