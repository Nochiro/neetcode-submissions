# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr_level = [root]
        ans = []    
        while curr_level:
            curr_value = []
            next_level = []
            for node in curr_level:
                curr_value.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                     next_level.append(node.right)  
            ans.append(curr_value)
            curr_level = next_level      
        return ans
