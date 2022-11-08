# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        if (root):
            stack = [root]
        ans   = []
        
        while(stack):
            current = stack.pop()
            
            ans.append(current.val)
            
            if (current.right):
                stack.append(current.right)
            if (current.left):
                stack.append(current.left)
            
        return ans
            
    
        
