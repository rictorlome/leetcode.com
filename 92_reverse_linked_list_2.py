# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev, cur, sublist_head, sublist_tail = None, head, head, head
        for i in range(n):
            nxt = cur.next
            if i + 2 == m:
                sublist_head = cur
            if i + 1 == m:
                sublist_tail = cur
            if m <= i + 1 <= n:
                cur.next = prev
            prev = cur
            cur = nxt
        sublist_head.next = prev
        sublist_tail.next = cur
        return head if m > 1 else prev