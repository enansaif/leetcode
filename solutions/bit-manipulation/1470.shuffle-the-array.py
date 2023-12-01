#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] << 32
        
        for i in range(n):
            x, y = nums[i], nums[i + n]
            n1, n2 = x, y
            n1, n2 = n1 >> 32, n2 >> 32
            nums[i*2], nums[i*2 + 1] = nums[i*2] | n1, nums[i*2 + 1] | n2
        
        for i in range(len(nums)):
            num = 0
            for j in range(32):
                num = num | (nums[i] & (1 << 31 - j))
            nums[i] = num
        return nums
        
# @lc code=end

