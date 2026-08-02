class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1 :return -1
        x,y=0,0
        while x < n:
            y=x+1
            while y!=n and nums[x]!=nums[y] : y+=1
            if y ==n: 
                x+=1
                y=x
            else: return nums[x]
        return -1

        