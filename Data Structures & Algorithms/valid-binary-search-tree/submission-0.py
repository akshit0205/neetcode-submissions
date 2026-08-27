# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Check(node,left,right):
            if not node: return True
            if not(left<node.val<right):return False
            return Check(node.left,left,node.val) and Check(node.right,node.val,right)
        return Check(root,float('-inf'),float('inf'))
        
