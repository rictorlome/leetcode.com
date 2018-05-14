# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur, which = self.getMin(root), 1
        while which < k:
            cur = self.successor(root,cur)
            which += 1
        return cur.val

    def getMin(self,root):
        cur = root
        while cur.left is not None:
            cur = cur.left
        return cur

    def lastLeft(self,root,node):
        cur, ll = root, None
        while cur.val is not node.val:
            if cur.val < node.val:
                cur = cur.right
            elif cur.val > node.val:
                ll = cur
                cur = cur.left
        return ll

    def successor(self,root,node):
        if node.right is None: return self.lastLeft(root,node)
        return self.getMin(node.right)
