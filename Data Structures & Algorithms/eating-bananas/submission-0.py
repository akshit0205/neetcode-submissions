class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest,left,right=max(piles),1,max(piles)
        while left <= right:
            mid=(left+right)//2
            res=0
            for x in piles:
                res+=math.ceil(x/mid)
            if res <= h :
                right=mid-1
                smallest=mid
            else : left=mid+1
        return smallest
