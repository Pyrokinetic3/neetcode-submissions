class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] in ['+', '-', '*', '/']:
                right = int(stack.pop())
                left = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(left + right)
                elif tokens[i] == '-':
                    stack.append(left - right)
                elif tokens[i] == '*':
                    stack.append(left * right)
                elif tokens[i] == '/':
                    stack.append(int(left / right))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[0]