class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        left,incre=0,len(s1)
        Count1,Count2=[0]*26,[0]*26
        for x in range(len(s1)):
            Count1[(ord(s1[x])-ord('a'))]+=1
            Count2[(ord(s2[x])-ord('a'))]+=1
        right = len(s1)
        if Count1==Count2: return True
        while right < len(s2):
            Count2[(ord(s2[left]))-ord('a')]-=1
            left+=1
            Count2[(ord(s2[right]))-ord('a')]+=1
            right+=1
            if Count1==Count2: return True
        return False    


        