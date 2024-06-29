class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = {0:-1}
        ones, zeros = 0, 0
        maxLn = 0
        for i, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                ones += 1
            d = zeros - ones
            if d in diff:
                maxLn = max(maxLn, i - diff[d])
            else:
                diff[d] = i
        return maxLn
        