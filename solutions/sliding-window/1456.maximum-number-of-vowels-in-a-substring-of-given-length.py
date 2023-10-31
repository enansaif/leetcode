#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {'a', 'e', 'i', 'o', 'u'}
        currCount, maxCount = 0, 0
        for i in range(k - 1):
            if s[i] in VOWELS:
                currCount += 1
        
        l, r = 0, k - 1
        while r < len(s):
            if s[r] in VOWELS:
                currCount += 1
            maxCount = max(currCount, maxCount)
            if s[l] in VOWELS:
                currCount -= 1
            r += 1
            l += 1
        return maxCount
        
# @lc code=end

