# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_num = root.val    
        def dfs(root, max_num):
            if root is None:
                return 0
            if root.val >= max_num:
                good = 1
               
            else:
                good = 0 
            new_max = max(root.val, max_num)    
            left = dfs(root.left, new_max)
            right = dfs(root.right, new_max)
            return good + left + right
        return dfs(root, max_num)            