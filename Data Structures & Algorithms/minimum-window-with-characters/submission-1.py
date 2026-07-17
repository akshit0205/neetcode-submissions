class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        have,need={},{}
        matches,res=0,""
        left=0
        minimum=float('inf')
        for x in t:
            need[x]=need.get(x,0)+1
        for right in range(len(s)):
            char=s[right]
            have[char]=have.get(char,0)+1
            if char in need and have[char]<=need[char]:
                matches+=1
            while matches==len(t):
                if (right-left+1)<minimum:
                    minimum=right-left+1
                    res=s[left:right+1]              
                left_char=s[left]
                have[left_char]-=1
                if left_char in need and have[left_char]<need[left_char]:
                    matches-=1
                left+=1
        return res
