# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return (
            self.greatest_in_subtree(root.left,root.val)
            and self.least_in_subtree(root.right,root.val)
            and self.isValidBST(root.right)
            and self.isValidBST(root.left)
        )

    def greatest_in_subtree(self,root,val):
        if root is None: return True
        return val > root.val and self.greatest_in_subtree(root.left,val) and self.greatest_in_subtree(root.right,val)

    def least_in_subtree(self,root,val):
        if root is None: return True
        return val < root.val and self.least_in_subtree(root.left,val) and self.least_in_subtree(root.right,val)


## Test Case below... Should return FALSE (30 < 45)

#         3
#          \
#          30
#         /
#       10
#         \
#          15
#           \
#            45

root = TreeNode(3)
root.right = TreeNode(30)
root.right.left = TreeNode(10)
root.right.left.right = TreeNode(15)
root.right.left.right.right = TreeNode(45)

s = Solution()
print(s.isValidBST(root)) #=> False
