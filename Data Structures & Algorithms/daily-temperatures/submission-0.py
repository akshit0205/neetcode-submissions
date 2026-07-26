class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
                while stack and stack[-1][0] < temp:
                    prev_temp,prev_ind=stack.pop()
                    res[prev_ind-1]=i+1-prev_ind
                stack.append((temp,i+1))
        return res

        