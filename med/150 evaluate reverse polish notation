class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # start from the right; that is the root node
        # the "first" one after the operator goes on the "left"
        # the "second" one after the right
        # you return the "rest" of the string
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b,
        }
        stack = []
        for i, token in enumerate(tokens):
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))
        return stack[-1]
