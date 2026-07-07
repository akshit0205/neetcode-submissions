class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        ans=[1]*len(nums)
        for x in range(len(nums)):
            ans[x]*=prefix
            prefix*=nums[x]
        postfix=1
        for x in range(len(nums)-1,-1,-1):
            ans[x]*=postfix
            postfix*=nums[x]
        return ans 