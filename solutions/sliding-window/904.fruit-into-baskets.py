#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        maxCount = 0
        l = 0
        for r in range(len(fruits)):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if not basket[fruits[l]]:
                    basket.pop(fruits[l])
                l += 1
            maxCount = max(maxCount, r - l + 1)
        return maxCount
        
# @lc code=end

