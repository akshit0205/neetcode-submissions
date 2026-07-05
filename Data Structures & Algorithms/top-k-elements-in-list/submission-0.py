class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for x in nums:
            hash[x]=hash.get(x,0)+1
        return sorted(hash,key=hash.get,reverse=True)[:k]