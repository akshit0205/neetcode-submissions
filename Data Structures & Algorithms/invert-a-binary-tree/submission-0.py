# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None or root.left == None and root.right==None: return root
        d=deque()
        d.append(root)
        while d:
            R=d.popleft()
            R.left,R.right=R.right,R.left
            if R.left: d.append(R.left)
            if R.right: d.append(R.right)
        return root
