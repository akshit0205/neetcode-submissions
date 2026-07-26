class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(speed)<=1: return len(speed)
        curr_time,fleet=0,0
        car=sorted(zip(position,speed),reverse=True)
        for p,s in car:
            travel=(target-p)/s
            if travel > curr_time:
                fleet+=1
                curr_time=travel  
        return fleet