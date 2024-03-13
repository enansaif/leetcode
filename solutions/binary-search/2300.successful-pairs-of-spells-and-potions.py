#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        def search(spell, potions, success):
            result = len(potions)
            l, r = 0, len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if potions[m] * spell >= success:
                    result = m
                    r = m - 1
                else:
                    l = m + 1
            return len(potions) - result
        
        result = []
        for spell in spells:
            result.append(search(spell, potions, success))
        return result
# @lc code=end

