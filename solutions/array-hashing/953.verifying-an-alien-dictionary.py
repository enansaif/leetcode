#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cmap = {c:i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            j = 0
            while j < len(prev):
                if j == len(curr) or cmap[prev[j]] > cmap[curr[j]]:
                    return False
                if cmap[prev[j]] < cmap[curr[j]]:
                    break
                j += 1
        return True
        
# @lc code=end

