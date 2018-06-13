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
        p_path, q_path = self.get_path(root,p,[])[1][::-1], self.get_path(root,q,[])[1][::-1]
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i].val == q_path[i].val:
            i += 1
        return p_path[i - 1]


    def get_path(self,root,node,path=[]):
        if root is None:
            return (False, path)
        elif root.val == node.val:
            path.append(root)
            return (True, path)
        l, r = self.get_path(root.left,node,path), self.get_path(root.right,node,path)
        if l[0] or r[0]:
            path.append(root)
            return (True, path)
        return (False, path)





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

print(s.lowestCommonAncestor(t,t.left,t.left.right.right))
