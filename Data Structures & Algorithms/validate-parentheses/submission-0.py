class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            # Opening bracket
            if ch in "({[":
                stack.append(ch)
            else:
                # Closing bracket: stack must not be empty
                if not stack:
                    return False
                # Top must match the corresponding opening
                if stack[-1] != matching[ch]:
                    return False
                stack.pop()
        
        # All opens must be closed
        return len(stack) == 0