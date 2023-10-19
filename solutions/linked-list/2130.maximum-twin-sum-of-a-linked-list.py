#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse list from mid point
        rHead = None
        while slow:
            temp = slow.next
            slow.next = rHead
            rHead = slow
            slow = temp
        
        # treverse list from both sides and calculate sum
        maxSum = 0
        while head and rHead:
            maxSum = max(maxSum, head.val + rHead.val)
            head = head.next
            rHead = rHead.next
        return maxSum
        
# @lc code=end

