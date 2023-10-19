#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        currSum = 0
        for i in range(k - 1):
            currSum += arr[i]
        
        count = 0
        l, r = 0, k - 1
        while r < len(arr):
            currSum += arr[r]
            count += 1 if (currSum / k) >= threshold else 0
            currSum -= arr[l]
            l += 1
            r += 1
        return count
    
# @lc code=end

