# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False       
            if root.val != subRoot.val:
                return False         
            return dfs(root.left,subRoot.left) and dfs(root.right, subRoot.right)       
        
        def containsSubTree(root, subRoot):
            if root is None: 
                return False
            return dfs(root, subRoot) or containsSubTree(root.right, subRoot) or containsSubTree(root.left, subRoot)
        return containsSubTree(root,subRoot)    
