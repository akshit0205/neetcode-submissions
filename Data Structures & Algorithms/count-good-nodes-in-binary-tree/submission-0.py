# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def Counting(node,path_maximum):
            if not node:
                return 0
            is_good=1 if node.val>=path_maximum else 0
            new_max=max(path_maximum,node.val)
            return is_good+Counting(node.left,new_max)+Counting(node.right,new_max)
        return Counting(root,root.val)