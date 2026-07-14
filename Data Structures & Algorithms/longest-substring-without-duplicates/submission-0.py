class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashs=set()
        left,right=0,0
        longest=0
        while right < len(s):
            while s[right] in hashs:
                hashs.remove(s[left])
                left+=1
            longest=max(longest,right-left+1)                
            hashs.add(s[right])
            right+=1
        return longest
        