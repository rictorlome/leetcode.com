# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None: return True
        if type(p) is not type(q): return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


#Example

root = TreeNode(68)
root.left = TreeNode(41)
root.left.left = TreeNode(-85)
root.left.left.right = TreeNode(49)
root.left.left.left = TreeNode(73)
root.left.left.left.left = TreeNode(98)
root.left.left.left.left.left = TreeNode(124)

oroot = TreeNode(68)
oroot.left = TreeNode(41)
oroot.left.left = TreeNode(-85)
oroot.left.left.right = TreeNode(49)
oroot.left.left.left = TreeNode(73)
oroot.left.left.left.left = TreeNode(98)
oroot.left.left.left.left.left = TreeNode(124)

s = Solution()
print(s.isSameTree(root,oroot))
