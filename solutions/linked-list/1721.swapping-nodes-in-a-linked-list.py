#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1 = n2 = tail = head
        i = k
        while i > 0:
            tail = tail.next
            i -= 1
        
        while tail:
            tail = tail.next
            n2 = n2.next
        
        while k > 1:
            n1 = n1.next
            k -= 1
        
        n1.val, n2.val = n2.val, n1.val
        return head
        
# @lc code=end

