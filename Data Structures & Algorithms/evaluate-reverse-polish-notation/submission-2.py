class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+" : lambda a, b : b + a,
            "-" : lambda a, b : b - a,
            "*" : lambda a, b : b *a,
            "/" : lambda a,b : int(b/a)
        }
        for ch in tokens:
            if ch in operations:
                a = stack.pop()
                b = stack.pop()
                value = operations[ch](a,b)
                stack.append(value)        
            else:
                c = int(ch)
                stack.append(c)

        return stack[-1]        