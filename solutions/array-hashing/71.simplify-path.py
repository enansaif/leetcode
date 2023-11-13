#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path += '/'
        currDir = ''
        for char in path:
            if char != '/':
                currDir += char
                continue
            if currDir == '':
                continue
            if currDir == '..':
                if stack:
                    stack.pop()
            elif currDir != '.':
                stack.append(currDir)
            currDir = ''
        return '/' + '/'.join(stack)
        
# @lc code=end

