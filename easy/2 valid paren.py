class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {"}": "{", ")": "(", "]": "["}
        openers = set("([{")
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                if not stack:
                    return False
                top = stack.pop()
                if top != closers[c]:
                    return False

        return not stack
