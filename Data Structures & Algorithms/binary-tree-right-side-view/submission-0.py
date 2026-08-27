# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        if not root.left and not root.right:return [root.val]
        ans=[]
        Q=deque()
        Q.append(root)
        while Q:
            level=len(Q)
            for i in range(level):
                node=Q.popleft()
                if node.left:Q.append(node.left)
                if node.right:Q.append(node.right)
                if i==level-1: ans.append(node.val)
        return ans