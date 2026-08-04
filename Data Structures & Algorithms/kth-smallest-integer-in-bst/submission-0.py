# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def inorder(node):
            nonlocal count
            if node is None:
                return    
            result = inorder(node.left)
            if result is not None:
                return result
            count += 1
            if count == k:
                return node.val  
            result = inorder(node.right)
            return result  
        return  inorder(root)    