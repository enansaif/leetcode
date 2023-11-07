#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#

# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        def dfs(i, isAlice, m):
            if (i, isAlice, m) in cache:
                return cache[(i, isAlice, m)]
            if i >= len(piles):
                return 0
            
            total = 0
            score = 0 if isAlice else float('inf')
            for j in range(2 * m):
                if i + j >= len(piles):
                    break
                total += piles[i + j]
                if isAlice:
                    score = max(dfs(i + j + 1, False, max(m, j + 1)) + total, score)
                else:
                    score = min(dfs(i + j + 1, True, max(m, j + 1)), score)
                cache[(i, isAlice, m)] = score
            return score
        return dfs(0, True, 1)
        
# @lc code=end

