class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,x in enumerate(nums):
            complement = target-x
            if complement in hash:
                return [hash[complement],i]
            hash[x]=i
        return [] 