class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights.append(0)
        res=0
        for i, height in enumerate(heights):
            while stack and height < stack[-1][0]:
                top_height,top_index=stack.pop()
                width=i-stack[-1][1]-1 if stack else i
                current_max=top_height*width
                res=max(current_max,res)
            stack.append((height,i))
        return res
        