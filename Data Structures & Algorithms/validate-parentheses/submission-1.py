class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={')':'(',']':'[','}':'{'}
        for x in s:
            if x in hash and stack and stack[-1]==hash[x]:
                stack.pop()
            else: stack.append(x)
        return not stack