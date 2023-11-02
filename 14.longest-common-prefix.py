#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass
        
# @lc code=end

# Horizontal scan solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = min(strs)
        for curStr in strs:
            r = 0
            while r < len(prefix):
                if prefix[r] != curStr[r]:
                    break
                r += 1
            prefix = prefix[:r]
        return prefix

