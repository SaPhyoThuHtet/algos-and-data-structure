# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        results = []
        stack = []
        if (root):
            stack = [root]
            
        while (stack):
            
            val = stack.pop()
            
            if (isinstance(val, int)):
                results.append(val)
            else:
                if (val.right):
                    stack.append(val.right)
                stack.append(val.val)
                if (val.left):
                    stack.append(val.left)
                    
        return results
