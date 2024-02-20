#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        sum_count = {}
        total = 0
        for n in nums:
            curr_sum += n
            if curr_sum == k:
                total += 1
            if curr_sum - k in sum_count:
                total += sum_count[curr_sum - k]
            
            sum_count[curr_sum] = sum_count.get(curr_sum, 0) + 1
           
        return total
        
# @lc code=end

