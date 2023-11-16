#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        maxWidth = 0
        while q:
            start = q[0][1]
            for _ in range(len(q)):
                node, end = q.popleft()
                maxWidth = max(maxWidth, end - start + 1)
                if node.left:
                    q.append((node.left, 2*end - 1))
                if node.right:
                    q.append((node.right, 2*end))

        return maxWidth
        
# @lc code=end

