# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None 

        root = TreeNode(preorder[0])
        
        root_idx = inorder.index(root.val)
        left_sub_in = inorder[:root_idx]
        right_sub_in = inorder[root_idx+1:]

        left_len = len(left_sub_in)

        left_sub_pre = preorder[1 : 1 + left_len]
        right_sub_pre = preorder[left_len + 1:]

        left = self.buildTree(left_sub_pre, left_sub_in)
        right = self.buildTree(right_sub_pre, right_sub_in) 

        root.left = left
        root.right = right
        return root
        
        
