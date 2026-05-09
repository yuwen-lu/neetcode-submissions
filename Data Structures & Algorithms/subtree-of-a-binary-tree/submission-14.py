# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        


        def sameTree(s, q):
            
            if not s and not q:
                return True
            elif s and q:

                if s.val != q.val:
                    return False
                else:
                    return sameTree(s.left, q.left) and sameTree(s.right, q.right)
            else:
                return False

        if not subRoot:
            return True
        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            