# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev, cur = node, node.next
        while cur.next is not None:
            prev.val = cur.val
            prev, cur = cur, cur.next
        prev.val = cur.val
        prev.next = None
