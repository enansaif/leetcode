#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can_reduce(num, arr):
            arr = arr.copy()
            for i in range(len(arr) - 1, 0, - 1):
                if arr[i] <= num:
                    continue
                arr[i - 1] += arr[i] - num
            return arr[0] <= num
        
        l, r = min(nums), max(nums)

        ans = 0
        while l <= r:
            m = (l + r) // 2
            if can_reduce(m, nums):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
        
# @lc code=end

