class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                a = stack.pop()
                b = stack.pop()
                value = b + a
                stack.append(value)
            elif ch == "-":
                a = stack.pop()
                b = stack.pop()
                value = b - a
                stack.append(value)
            elif ch == "*":
                a = stack.pop()
                b = stack.pop()
                value = b * a
                stack.append(value)
            elif ch == "/":
                a = stack.pop()
                b = stack.pop()
                value = int(b / a)
                stack.append(value)        
            else:
                c = int(ch)
                stack.append(c)

        return stack[-1]        