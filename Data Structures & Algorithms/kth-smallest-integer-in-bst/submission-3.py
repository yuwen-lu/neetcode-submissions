# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if self.leftCount(root) == k - 1:
            return root.val
        elif self.leftCount(root) > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - self.leftCount(root) -1)


    def leftCount(self, root: Optional[TreeNode]) -> int:
        if root and root.left:
            return self.subtreeCount(root.left)
        else:
            return 0
        

    def subtreeCount(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return (1 + self.subtreeCount(root.left) + self.subtreeCount(root.right))
        