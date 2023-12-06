#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])
        N = 1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == N - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            N *= 2
        return root
        
# @lc code=end

