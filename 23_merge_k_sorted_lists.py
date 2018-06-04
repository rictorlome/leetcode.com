from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h, res = [], None
        for k, head in enumerate(lists):
            ## tuple (val, k, node)
            if head is not None:
                heappush(h, (head.val, k, head))

        while len(h) > 0:
            val, k, node = heappop(h)
            if res is None:
                res = node
                cur = res
            else:
                cur.next = node
                cur = cur.next
            if node.next is not None:
                heappush(h, (node.next.val, k, node.next))
        return res
