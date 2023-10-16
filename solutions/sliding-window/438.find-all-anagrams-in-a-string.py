#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        chrArrP, chrArrS = [0] * 26, [0] * 26
        for i in range(len(p)):
            chrArrP[ord(p[i]) - ord('a')] += 1
        for i in range(len(p) - 1):
            chrArrS[ord(s[i]) - ord('a')] += 1
        
        result = []
        l, r = 0, len(p) - 1
        while r < len(s):
            chrArrS[ord(s[r]) - ord('a')] += 1
            if chrArrS == chrArrP:
                result.append(l)
            chrArrS[ord(s[l]) - ord('a')] -= 1
            r += 1
            l += 1
        return result
# @lc code=end

