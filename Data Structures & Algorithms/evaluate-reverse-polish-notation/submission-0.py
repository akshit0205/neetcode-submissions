class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack=[]
        res=0
        for ch in tokens:
            if ch.lstrip('-').isdigit() :
                Stack.append(int(ch))
            elif ch == '+':
                x=Stack.pop()
                res=x+Stack.pop()
                Stack.append(res)
            elif ch == '-':
                x=Stack.pop()
                res=Stack.pop()-x
                Stack.append(res)
            elif ch == '/':
                x=Stack.pop()
                res=int(Stack.pop()/x)
                Stack.append(res)
            elif ch == '*':
                x=Stack.pop()
                res=Stack.pop()*x
                Stack.append(res)
        return Stack[-1]
        