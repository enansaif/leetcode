#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(l, r, isAlice):
            if (l, r, isAlice) in cache:
                return cache[(l, r, isAlice)]
            if l > r:
                return 0
            left = dfs(l + 1, r, not isAlice)
            right = dfs(l, r - 1, not isAlice)
            if isAlice:
                score = max(left + piles[l], right + piles[r])
                cache[(l, r, isAlice)] = score
                return cache[(l, r, isAlice)]
            cache[(l, r, isAlice)] = min(left, right)
            return cache[(l, r, isAlice)]
        score = dfs(0, len(piles) - 1, True)
        return score > sum(piles) / 2
        
# @lc code=end

