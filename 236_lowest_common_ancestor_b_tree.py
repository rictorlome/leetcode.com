# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        if root is q or root is p: return root
        l,r = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
        if l and r: return root
        if not l and not r: return None
        return l if l else r

s = Solution()

#      _______3______
#     /              \
#  ___5__          ___1__
# /      \        /      \
# 6      _2       0       8
#       /  \
#       7   4

t = TreeNode(3,
        TreeNode(5,
            TreeNode(6),
            TreeNode(2,
                TreeNode(7),
                TreeNode(4))),
        TreeNode(1,
            TreeNode(0),
            TreeNode(8)))

print(s.lowestCommonAncestor(t,t.left,t.left.right))
