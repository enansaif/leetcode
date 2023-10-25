#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            if n == 1:
                leafNode = Node(grid[r][c], 1, None, None, None, None)
                return leafNode
            
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)
            
            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
                and (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val)):
                return Node(topLeft.val, 1, None, None, None, None)
            
            newNode = Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
            return newNode
        return dfs(len(grid), 0, 0)
                
        
# @lc code=end

