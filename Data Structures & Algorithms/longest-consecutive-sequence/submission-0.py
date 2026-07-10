class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        hash=set(nums)
        for x in hash:
            if (x-1) in hash:
                continue
            current_length=1
            while (x+current_length) in hash:
                current_length+=1
            longest=max(longest,current_length)
        return longest