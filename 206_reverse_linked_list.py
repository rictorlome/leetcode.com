# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur = rest_head = self.reverseList(head.next)
        while cur.next:
            cur = cur.next
        head.next = None
        cur.next = head
        return rest_head