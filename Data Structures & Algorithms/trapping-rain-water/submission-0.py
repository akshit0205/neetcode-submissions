class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left,max_right=[0]*n,[0]*n
        left,right,max_water=0,0,0
        for i in range(n):
            max_left[i]=left
            left=max(left,height[i])
        for i in range(n-1,-1,-1):
            max_right[i]=right
            right=max(right,height[i])
        for i in range(n):
            water=min(max_left[i],max_right[i])-height[i]
            if water>0 : max_water+=water
        return max_water


