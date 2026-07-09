class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
                        ")": "(",
                        "]": "[",
                        "}": "{"
                    }
        stack = []
        for ch in s:    
            if ch in matching:
                if not stack:
                    return False
                if stack[-1] == matching[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack
               