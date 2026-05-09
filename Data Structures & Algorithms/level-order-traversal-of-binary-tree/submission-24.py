# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        result = []

        while q:
            result.append([i.val for i in q])
            q_len = len(q)
            for i in range(q_len):
                item = q.popleft()
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
        return result
