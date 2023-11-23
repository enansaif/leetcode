#
# @lc app=leetcode id=1849 lang=python3
#
# [1849] Splitting a String Into Descending Consecutive Values
#

# @lc code=start
class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i, prev):
            if i == len(s):
                return True
            if prev == 0:
                return False
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                num = int(curr)
                if j == len(s) - 1 and prev == -1:
                    continue
                if prev != -1 and prev - num != 1:
                    continue
                if dfs(j + 1, num):
                    return True
            return False
        return dfs(0, -1)
        
# @lc code=end

