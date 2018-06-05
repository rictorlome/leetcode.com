# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        if self.next is None: return str(self.val)
        return str(self.val) + '->' + self.next.__repr__()

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_head, more_head = ListNode(-1), ListNode(-1)
        less_cur, more_cur = less_head, more_head

        cur = head
        while cur is not None:
            if cur.val < x:
                less_cur.next = cur
                less_cur = less_cur.next
            else:
                more_cur.next = cur
                more_cur = more_cur.next
            cur = cur.next

        less_cur.next, more_cur.next = more_head.next, None
        return less_head.next

s = Solution()
ex = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
print(s.partition(ex,3))
