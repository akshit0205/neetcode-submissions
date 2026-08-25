# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSame(self,a,b):
        if not a and not b: return True
        if not a or not b or a.val != b.val:return False
        return self.isSame(a.left,b.left) and self.isSame(a.right,b.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: return False
        Q=deque()
        X=root
        Q.append(X)
        while Q:
            curr=Q.popleft()
            if curr.val == subRoot.val: 
                if self.isSame(curr,subRoot):return True
            if curr.left: Q.append(curr.left)
            if curr.right: Q.append(curr.right)
        return False