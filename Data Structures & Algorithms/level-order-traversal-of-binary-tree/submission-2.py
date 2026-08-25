# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root : return ans
        Q=deque()
        Q.append(root)
        while Q:
            L=[]
            for i in range(0,len(Q)):
                if not Q: break
                X=Q.popleft()
                L.append(X.val)
                if X.left:Q.append(X.left)
                if X.right:Q.append(X.right)
            ans.append(L)
        return ans


