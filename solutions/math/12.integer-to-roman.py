#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        intToSign = [('M', 1000), ('CM', 900), ('D', 500), 
                     ('CD', 400), ('C', 100), ('XC', 90),
                     ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
                     ('V', 5), ('IV', 4), ('I', 1)]
        
        curr_num = num
        curr_str = ''
        for sign, value in intToSign:
            repeat, curr_num = curr_num // value, curr_num % value
            curr_str += sign * repeat
        return curr_str
        
# @lc code=end

